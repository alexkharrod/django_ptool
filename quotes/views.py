import base64
import os
import tempfile
from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.timezone import now
from weasyprint import HTML

from .forms import CreateQuoteForm
from .models import Quote

# Create your views here.


# home view
def home(request):
    return render(request, "index.html")


def view_quote(request, pk):
    quote = Quote.objects.get(pk=pk)
    return render(request, "view_quote.html", {"quote": quote})

def edit_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == "POST":
        form = CreateQuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect("view_quote", pk=quote.pk)
    else:
        form = CreateQuoteForm(instance=quote)
    return render(request, "edit_quote.html", {"form": form, "quote": quote})


def quotes(request):
    # get the search query from the GET parameters
    search_query = request.GET.get("search", "")

    # Start with all quotes
    queryset = Quote.objects.all()

    # Apply search if there is a search query
    if search_query:
        queryset = queryset.filter(
            Q(quote_num__icontains=search_query)
            | Q(name__icontains=search_query)
            | Q(category__icontains=search_query)
            | Q(customer_name__icontains=search_query)
            | Q(sales_rep__icontains=search_query)
        )
    queryset = queryset.order_by("quote_num")
    paginator = Paginator(queryset, 25)
    # Get the page number from the request
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "quotes": queryset,
        "search_query": search_query,
    }

    return render(request, "quotes.html", context)


def create_quote(request):
    if request.method == "POST":
        form = CreateQuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            messages.success(request, "Quote created successfully!")
            return redirect(
                "view_quote", pk=quote.pk
            )  # Replace with your desired redirect view
        else:
            messages.error(
                request,
                "There was an error creating the quote. Please check the form and try again.",
            )
    else:
        # Generate the quote number
        date_prefix = now().strftime("%m%d%y")  # Generate MMDDYY
        last_quote = (
            Quote.objects.filter(quote_num__startswith=date_prefix)
            .order_by("-quote_num")
            .first()
        )
        if last_quote:
            last_suffix = int(last_quote.quote_num[-4:])  # Extract numeric suffix
            new_suffix = f"{last_suffix + 1:02d}"  # Increment suffix, zero-padded
        else:
            new_suffix = "0001"  # Start at 0001 if no quotes exist for the day
        auto_generated_quote_num = f"{date_prefix}{new_suffix}"

        # Pass the auto-generated quote number as the initial value
        form = CreateQuoteForm(initial={"quote_num": auto_generated_quote_num})

    return render(request, "create_quote.html", {"form": form})


def quote_pdf(request, quote_id):
    quote = Quote.objects.get(id=quote_id)

    # Get the absolute path for the image
    image_path = os.path.join(settings.BASE_DIR, "static", "images", quote.image_url)

    # Read and encode the image
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

    context = {"quote": quote, "encoded_image": encoded_image}

    html_string = render_to_string("quote_pdf.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="quote_{quote.quote_num}.pdf"'
    )

    HTML(string=html_string, base_url=request.build_absolute_uri("/")).write_pdf(
        response, presentational_hints=True
    )

    return response

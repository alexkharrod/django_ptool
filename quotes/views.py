from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.timezone import now
from .models import Quote

from .forms import CreateQuoteForm

# Create your views here.


# home view
def home(request):
    return render(request, "index.html")


def create_quote(request):
    if request.method == "POST":
        form = CreateQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Quote created successfully!")
            return redirect("home")  # Replace with your desired redirect view
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
            new_suffix = f"{last_suffix + 1:04d}"  # Increment suffix, zero-padded
        else:
            new_suffix = "0001"  # Start at 0001 if no quotes exist for the day
        auto_generated_quote_num = f"{date_prefix}{new_suffix}"

        # Pass the auto-generated quote number as the initial value
        form = CreateQuoteForm(initial={"quote_num": auto_generated_quote_num})

    return render(request, "create_quote.html", {"form": form})

import base64
import os
from pathlib import Path

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from weasyprint import HTML

from .forms import CreateProductForm
from .models import Product

# Create your views here.


# home view
def home(request):
    return render(request, "index.html")


def view_product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "view_product.html", {"product": product})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CreateProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("view_product", pk=product.pk)
    else:
        form = CreateProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form, "product": product})


def products(request):
    # Get the search query and status filter from GET parameters
    search_query = request.GET.get("search", "")
    status_filter = request.GET.get("status", "Open")  # Default to 'Open'

    # Start with all products
    queryset = Product.objects.all()

    # Apply status filter
    if status_filter:
        queryset = queryset.filter(status=status_filter)

    # Apply search if there is a search query
    if search_query:
        queryset = queryset.filter(
            Q(sku__icontains=search_query)
            | Q(name__icontains=search_query)
            | Q(category__icontains=search_query)
        )

    # Order by SKU or any other field you prefer
    queryset = queryset.order_by("sku")

    context = {
        "products": queryset,
        "search_query": search_query,
        "status_filter": status_filter,
    }

    return render(request, "products.html", context)


def add_product(request):
    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            product = form.save()
            return redirect("view_product", pk=product.pk)

    else:
        form = CreateProductForm()
    return render(request, "add_product.html", {"form": form})


def npds(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get the absolute path for the image
    image_path = os.path.join(settings.BASE_DIR, "static", "images", product.image_url)

    # Read and encode the image
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

    context = {"product": product, "encoded_image": encoded_image}

    html_string = render_to_string("npds.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="NPDS_{product.sku}.pdf"'

    HTML(string=html_string, base_url=request.build_absolute_uri("/")).write_pdf(
        response, presentational_hints=True
    )

    return response

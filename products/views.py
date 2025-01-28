from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateProductForm
from .models import Product

# Create your views here.


# home view
def home(request):
    return render(request, "index.html")


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = CreateProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
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
            form.save()
            return redirect("products")

    else:
        form = CreateProductForm()
    return render(request, "add_product.html", {"form": form})

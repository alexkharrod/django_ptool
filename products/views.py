from django.shortcuts import render

from .forms import CreateProductForm

# Create your views here.


# home view
def home(request):
    return render(request, "index.html")


def add_product(request):
    form = CreateProductForm()
    return render(request, "add_product.html", {"form": form})

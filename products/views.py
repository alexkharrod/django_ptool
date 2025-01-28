from django.shortcuts import redirect, render

from .forms import CreateProductForm

# Create your views here.


# home view
def home(request):
    return render(request, "index.html")


def add_product(request):

    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("home")

    else:
        form = CreateProductForm()
    return render(request, "add_product.html", {"form": form})

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from products.forms import CreateProductForm
from .forms import ProspectForm
from .models import Prospect


def scouting_list(request):
    search_query = request.GET.get("search", "")
    status_filter = request.GET.get("status", "")
    show_filter = request.GET.get("show", "")

    queryset = Prospect.objects.all()

    if status_filter:
        queryset = queryset.filter(status=status_filter)

    if show_filter:
        queryset = queryset.filter(show_name__icontains=show_filter)

    if search_query:
        queryset = queryset.filter(
            Q(product_name__icontains=search_query)
            | Q(vendor_name__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(show_name__icontains=search_query)
        )

    # Unique show names for filter dropdown
    shows = Prospect.objects.values_list("show_name", flat=True).distinct().order_by("show_name")

    context = {
        "prospects": queryset,
        "search_query": search_query,
        "status_filter": status_filter,
        "show_filter": show_filter,
        "shows": shows,
        "status_choices": Prospect.STATUS_CHOICES,
    }
    return render(request, "scouting_list.html", context)


def scouting_detail(request, pk):
    prospect = get_object_or_404(Prospect, pk=pk)
    return render(request, "scouting_detail.html", {"prospect": prospect})


def scouting_add(request):
    if request.method == "POST":
        form = ProspectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("scouting_list")
    else:
        # Pre-fill show name if passed via query param
        initial = {}
        if request.GET.get("show"):
            initial["show_name"] = request.GET.get("show")
        form = ProspectForm(initial=initial)
    return render(request, "scouting_add.html", {"form": form})


def scouting_edit(request, pk):
    prospect = get_object_or_404(Prospect, pk=pk)
    if request.method == "POST":
        form = ProspectForm(request.POST, request.FILES, instance=prospect)
        if form.is_valid():
            form.save()
            return redirect("scouting_detail", pk=prospect.pk)
    else:
        form = ProspectForm(instance=prospect)
    return render(request, "scouting_edit.html", {"form": form, "prospect": prospect})


def scouting_promote(request, pk):
    """Pre-fills the Add Product form with scouting data."""
    prospect = get_object_or_404(Prospect, pk=pk)

    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            # Mark prospect as promoted
            prospect.promoted = True
            prospect.promoted_sku = product.sku
            prospect.status = "Adding"
            prospect.save(update_fields=["promoted", "promoted_sku", "status"])
            return redirect("view_product", pk=product.pk)
    else:
        # Map scouting fields → product fields
        initial = {
            "name": prospect.product_name,
            "vendor": prospect.vendor_name,
            "description": prospect.description,
            "colors": prospect.colors,
            "production_time": prospect.lead_time,
            "status": "Open",
        }
        form = CreateProductForm(initial=initial)

    return render(
        request,
        "scouting_promote.html",
        {"form": form, "prospect": prospect},
    )

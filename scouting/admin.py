from django.contrib import admin

from .models import Prospect


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "vendor_name",
        "show_name",
        "unit_cost",
        "status",
        "promoted",
        "date_added",
    )
    list_filter = ("status", "show_name", "promoted")
    search_fields = ("product_name", "vendor_name", "show_name", "description")
    readonly_fields = ("date_added", "date_updated")

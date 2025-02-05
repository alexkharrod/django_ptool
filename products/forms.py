from django import forms

from .models import Product  # Import the Product model


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "sku",
            "name",
            "category",
            "image_url",
            "moq",
            "package",
            "production_time",
            "estimated_launch",
            "description",
            "vendor",
            "vendor_sku",
            "carton_qty",
            "carton_weight",
            "carton_width",
            "carton_length",
            "carton_height",
            "imprint_location",
            "imprint_method",
            "imprint_dimension",
            "air_freight",
            "ocean_freight",
            "duty_percent",
            "tariff_percent",
            "price_list",
            "product_list",
            "hts_list",
            "npds_done",
            "qb_added",
            "published",
            "status",
            "colors",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }

        labels = {
            "sku": "SKU",
            "name": "Product Name",
            "category": "Category",
            "image_url": "Image URL",
            "moq": "MOQ",
            "package": "Package",
            "production_time": "Production Time",
            "estimated_launch": "Estimated Launch",
            "description": "Specifications",
            "vendor": "Vendor",
            "vendor_sku": "Vendor SKU",
            "carton_qty": "Carton Quantity",
            "carton_weight": "Carton Weight",
            "carton_width": "Carton Width",
            "carton_length": "Carton Length",
            "carton_height": "Carton Height",
            "imprint_location": "Imprint Location",
            "imprint_method": "Imprint Method",
            "imprint_dimension": "Imprint Dimension",
            "air_freight": "Air Freight",
            "ocean_freight": "Ocean Freight",
            "duty_percent": "Duty Percent",
            "tariff_percent": "Tariff Percent",
            "price_list": "Price List",
            "product_list": "Product List",
            "hts_list": "Added to HTS",
            "npds_done": "NPDS Done",
            "qb_added": "QB Added",
            "published": "Published",
            "status": "Status",
            "colors": "Colors",
        }

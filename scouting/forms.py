from django import forms

from .models import Prospect


class ProspectForm(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = [
            "show_name",
            "show_date",
            "vendor_name",
            "vendor_contact",
            "vendor_email",
            "vendor_website",
            "product_name",
            "description",
            "unit_cost",
            "colors",
            "lead_time",
            "notes",
            "image",
            "status",
        ]

        widgets = {
            "show_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "notes": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }

        labels = {
            "show_name": "Show / Event",
            "show_date": "Show Date",
            "vendor_name": "Vendor Name",
            "vendor_contact": "Vendor Contact",
            "vendor_email": "Vendor Email",
            "vendor_website": "Vendor Website",
            "product_name": "Product Name / Description",
            "description": "Specifications",
            "unit_cost": "Unit Cost (as seen)",
            "colors": "Colors Available",
            "lead_time": "Lead Time",
            "notes": "Additional Notes",
            "image": "Product Photo",
            "status": "Status",
        }

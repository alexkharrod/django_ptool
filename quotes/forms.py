from django import forms

from .models import Quote


class CreateQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            "quote_num",
            "name",
            "vendor",
            "vendor_part_number",
            "category",
            "image_url",
            "moq",
            "package",
            "production_time",
            "description",
            "air_freight",
            "ocean_freight",
            "duty_percent",
            "tariff_percent",
            "imprint_cost",
            "customer_name",
            "sales_rep",
            "carton_qty",
            "carton_weight",
            "carton_width",
            "carton_length",
            "carton_height",
            "imprint_location",
            "imprint_method",
            "imprint_dimension",
            "quantity1",
            "quantity2",
            "quantity3",
            "quantity4",
            "quantity5",
            "qty1_cost",
            "qty2_cost",
            "qty3_cost",
            "qty4_cost",
            "qty5_cost",
            "qty1_price_air",
            "qty2_price_air",
            "qty3_price_air",
            "qty4_price_air",
            "qty5_price_air",
            "qty1_price_ocean",
            "qty2_price_ocean",
            "qty3_price_ocean",
            "qty4_price_ocean",
            "qty5_price_ocean",
            "status",
            "air_transit_time",
            "ocean_transit_time",
            "notes",
            "reciprocal_tariffs",
        ]
        widgets = {
            "air_freight": forms.TextInput(attrs={"class": "form-control"}),
            "ocean_freight": forms.TextInput(attrs={"class": "form-control"}),
            "air_transit_time": forms.TextInput(attrs={"class": "form-control"}),
            "ocean_transit_time": forms.TextInput(attrs={"class": "form-control"}),
            "notes": forms.TextInput(attrs={"class": "form-control"}),
            "reciprocal_tariffs": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "quote_num": forms.TextInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
            'status': forms.Select(choices=Quote.STATUS_CHOICES, attrs={'class': 'form-control'}),
        }

        labels = {
            "quote_num": "Quote Number",
            "name": "Product Name",
            "vendor": "Vendor Name",
            "vendor_part_number": "Vendor Part Number",
            "category": "Product Category",
            "image_url": "Product Image URL",
            "moq": "Minimum Order Quantity (MOQ)",
            "package": "Package Type",
            "production_time": "Production Time",
            "description": "Product Description",
            "duty_percent": "Duty Percentage",
            "tariff_percent": "Tariff Percentage",
            "imprint_cost": "Imprint Cost",
            "customer_name": "Customer Name",
            "sales_rep": "Sales Representative",
            "carton_qty": "Carton Quantity",
            "carton_weight": "Carton Weight (kg)",
            "carton_width": "Carton Width (cm)",
            "carton_length": "Carton Length (cm)",
            "carton_height": "Carton Height (cm)",
            "imprint_location": "Imprint Location",
            "imprint_method": "Imprint Method",
            "imprint_dimension": "Imprint Dimension (cm)",
            "quantity1": "Quantity Level 1",
            "quantity2": "Quantity Level 2",
            "quantity3": "Quantity Level 3",
            "quantity4": "Quantity Level 4",
            "quantity5": "Quantity Level 5",
            "qty1_cost": "Cost for Quantity 1",
            "qty2_cost": "Cost for Quantity 2",
            "qty3_cost": "Cost for Quantity 3",
            "qty4_cost": "Cost for Quantity 4",
            "qty5_cost": "Cost for Quantity 5",
            "qty1_price_air": "Price Air for Quantity 1",
            "qty2_price_air": "Price Air for Quantity 2",
            "qty3_price_air": "Price Air for Quantity 3",
            "qty4_price_air": "Price Air for Quantity 4",
            "qty5_price_air": "Price Air for Quantity 5",
            "qty1_price_ocean": "Price Ocean for Quantity 1",
            "qty2_price_ocean": "Price Ocean for Quantity 2",
            "qty3_price_ocean": "Price Ocean for Quantity 3",
            "qty4_price_ocean": "Price Ocean for Quantity 4",
            "qty5_price_ocean": "Price Ocean for Quantity 5",
            "status": "Status",
            "air_transit_time": "Air Transit Time",
            "ocean_transit_time": "Ocean Transit Time",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.initial.update(
                {
                    "air_transit_time": "7-10 days",
                    "ocean_transit_time": "~6 weeks",
                    "quote_num": "Q12345",  # Default quote number
                    "name": "Default Product Name",
                    "vendor": "Default Vendor",
                    "vendor_part_number": "12345",
                    "category": "Default Category",
                    "image_url": "https://example.com/image.jpg",
                    "moq": 100,
                    "package": "Default Package",
                    "production_time": "7 days",
                    "description": "Default description for the product.",
                    "air_freight": 0.0,
                    "ocean_freight": 0.0,
                    "duty_percent": 10.0,
                    "tariff_percent": 5.0,
                    "imprint_cost": 50.0,
                    "customer_name": "Default Customer",
                    "sales_rep": "Default Sales Rep",
                    "carton_qty": 10,
                    "carton_weight": 1.5,
                    "carton_width": 30.0,
                    "carton_length": 40.0,
                    "carton_height": 50.0,
                    "imprint_location": "Default Imprint Location",
                    "imprint_method": "Default Imprint Method",
                    "imprint_dimension": "10x10 cm",
                    "quantity1": 100,
                    "quantity2": 200,
                    "quantity3": 300,
                    "quantity4": 400,
                    "quantity5": 500,
                    "qty1_cost": 10.0,
                    "qty2_cost": 9.5,
                    "qty3_cost": 9.0,
                    "qty4_cost": 8.5,
                    "qty5_cost": 8.0,
                    "qty1_price_air": 20.0, # Default example value
                    "qty2_price_air": 19.5, # Default example value
                    "qty3_price_air": 19.0,
                    "qty4_price_air": 18.5,
                    "qty5_price_air": 18.0,
                    "qty1_price_ocean": 0.0,
                    "qty2_price_ocean": 0.0,
                    "qty3_price_ocean": 0.0,
                    "qty4_price_ocean": 0.0,
                    "qty5_price_ocean": 0.0,
                }
            )

    def clean(self):
        cleaned_data = super().clean()

        # Only perform validation if price fields are present in the data
        if 'qty1_price_air' in self.data or 'qty1_price_ocean' in self.data:
            price_air_q1 = cleaned_data.get("qty1_price_air")
            price_ocean_q1 = cleaned_data.get("qty1_price_ocean")

            # Check if both Q1 price fields are empty or None (or effectively zero)
            is_air_q1_missing = price_air_q1 is None or float(price_air_q1) == 0.0
            is_ocean_q1_missing = price_ocean_q1 is None or float(price_ocean_q1) == 0.0

            if is_air_q1_missing and is_ocean_q1_missing:
                raise forms.ValidationError(
                    "At least one price (Air or Ocean) must be provided for Quantity Level 1."
                )

        # No validation needed for Q2-Q5 as per requirements

        return cleaned_data

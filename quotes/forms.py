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
            "qty1_price",
            "qty2_price",
            "qty3_price",
            "qty4_price",
            "qty5_price",
            "status",
        ]
        widgets = {
            "air_freight": forms.TextInput(attrs={"class": "form-control"}),
            "ocean_freight": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "quote_num": forms.TextInput(
                attrs={"readonly": "readonly", "class": "form-control"}
            ),
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
            "qty1_price": "Price for Quantity 1",
            "qty2_price": "Price for Quantity 2",
            "qty3_price": "Price for Quantity 3",
            "qty4_price": "Price for Quantity 4",
            "qty5_price": "Price for Quantity 5",
            "status": "Status",
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.initial.update(
                {
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
                    "qty1_price": 20.0,
                    "qty2_price": 19.5,
                    "qty3_price": 19.0,
                    "qty4_price": 18.5,
                    "qty5_price": 18.0,
                }
            )

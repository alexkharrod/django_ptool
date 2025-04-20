from django.apps import apps
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now


# Create your models here.
class Quote(models.Model):
    quote_num = models.CharField(max_length=20, unique=True, null=False)
    name = models.CharField(max_length=150, default="Product Name")
    vendor = models.CharField(max_length=50, default="Vendor Name")
    vendor_part_number = models.CharField(max_length=50, default="Vendor Part Number")
    category = models.CharField(max_length=50, default="Category")
    image_url = models.CharField(
        max_length=2083, default="https://via.placeholder.com/150"
    )
    moq = models.IntegerField(default=0)
    package = models.CharField(max_length=50, default="White Box")
    production_time = models.CharField(max_length=50, default="MUST BE SPECIFIED")
    description = models.TextField(max_length=500, default="Description")

    customer_name = models.CharField(max_length=50, default="Customer Name")
    sales_rep = models.CharField(max_length=50, default="Sales Rep")

    # Master Carton info:
    carton_qty = models.IntegerField(default=0)
    carton_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    carton_width = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    carton_length = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    carton_height = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    # Imprint info:
    imprint_location = models.CharField(max_length=50, default="Imprint Location")
    imprint_method = models.CharField(max_length=50, default="Imprint Method")
    imprint_dimension = models.CharField(max_length=50, default="Imprint Dimension")

    # Freight and Tariff Info:
    air_freight = models.TextField(max_length=500, default="Air Freight")
    ocean_freight = models.TextField(max_length=500, default="Ocean Freight")
    duty_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tariff_percent = models.DecimalField(max_digits=10, decimal_places=2, default=25.0)
    imprint_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.05)

    # Cost and Quote Fields:
    # quantities for quote
    quantity1 = models.IntegerField(default=0)
    quantity2 = models.IntegerField(default=0)
    quantity3 = models.IntegerField(default=0)
    quantity4 = models.IntegerField(default=0)
    quantity5 = models.IntegerField(default=0)

    # Unit Costs
    qty1_cost = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    qty2_cost = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    qty3_cost = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    qty4_cost = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    qty5_cost = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)

    # Price via Air
    qty1_price_air = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty2_price_air = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty3_price_air = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty4_price_air = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty5_price_air = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)

    # Price via Ocean
    qty1_price_ocean = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty2_price_ocean = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty3_price_ocean = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty4_price_ocean = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)
    qty5_price_ocean = models.DecimalField(max_digits=10, decimal_places=3, default=0.0, blank=True, null=True)

    # Quote created data: DD-MM_YYYY
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Added', 'Added'),
        ('Closed', 'Closed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Open')
    date_created = models.DateTimeField(default=now, null=False, blank=False)

    air_transit_time = models.CharField(max_length=50, default="7-10 days")
    ocean_transit_time = models.CharField(max_length=50, default="~6 weeks")

    def __str__(self):
        return self.quote_num

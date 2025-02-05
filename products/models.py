from django.db import models


# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=20, unique=True, null=False)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
    moq = models.IntegerField()
    package = models.CharField(max_length=50)
    production_time = models.CharField(max_length=50)
    estimated_launch = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    # Vendor info:
    vendor = models.CharField(max_length=50)
    vendor_sku = models.CharField(max_length=50)

    # Master Carton info:
    carton_qty = models.IntegerField()
    carton_weight = models.DecimalField(max_digits=10, decimal_places=2)
    carton_width = models.DecimalField(max_digits=10, decimal_places=2)
    carton_length = models.DecimalField(max_digits=10, decimal_places=2)
    carton_height = models.DecimalField(max_digits=10, decimal_places=2)

    # Imprint info:
    imprint_location = models.CharField(max_length=50)
    imprint_method = models.CharField(max_length=50)
    imprint_dimension = models.CharField(max_length=50)

    # Freight Costs
    air_freight = models.DecimalField(max_digits=10, decimal_places=2)
    ocean_freight = models.DecimalField(max_digits=10, decimal_places=2)
    duty_percent = models.DecimalField(max_digits=10, decimal_places=2)
    tariff_percent = models.DecimalField(max_digits=10, decimal_places=2)

    # To add checkboxes:
    price_list = models.BooleanField(default=False)
    product_list = models.BooleanField(default=False)
    hts_list = models.BooleanField(default=False)
    npds_done = models.BooleanField(default=False)
    qb_added = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    colors = models.CharField(max_length=150)

    # Product Status
    status = models.CharField(max_length=50)

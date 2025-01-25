from django.db import models


# Create your models here.
class Quote(models.Model):
    quote_num = models.CharField(max_length=20, unique=True,null=False)
    name = models.CharField(max_length=150)
    vendor = models.CharField(max_length=50)
    vendor_part_number = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    moq = models.IntegerField()
    package = models.CharField(max_length=50)
    production_time = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    duty_percent = models.DecimalField(max_digits=10, decimal_places=2)
    tariff_percent = models.DecimalField(max_digits=10, decimal_places=2)
    imprint_cost = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=50)
    sales_rep = models.CharField(max_length=50)

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

   # Cost and Quote Fields:
   # quantities for quote
    quantity1 = models.IntegerField()
    quantity2 = models.IntegerField()
    quantity3 = models.IntegerField()
    quantity4 = models.IntegerField()
    quantity5 = models.IntegerField()
    
   # Unit Costs
    qty1_cost = models.DecimalField(max_digits=10, decimal_places=2)
    qty2_cost = models.DecimalField(max_digits=10, decimal_places=2)
    qty3_cost = models.DecimalField(max_digits=10, decimal_places=2)
    qty4_cost = models.DecimalField(max_digits=10, decimal_places=2)
    qty5_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Quote PRICES
    qty1_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty2_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty3_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty4_price = models.DecimalField(max_digits=10, decimal_places=2)
    qty5_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Quote created data: DD-MM_YYYY
    
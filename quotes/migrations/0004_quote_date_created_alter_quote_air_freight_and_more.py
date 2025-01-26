# Generated by Django 4.2.18 on 2025-01-26 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_remove_quote_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='quote',
            name='air_freight',
            field=models.TextField(default='Air Freight', max_length=500),
        ),
        migrations.AlterField(
            model_name='quote',
            name='carton_height',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='carton_length',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='carton_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='carton_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='carton_width',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='category',
            field=models.CharField(default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='customer_name',
            field=models.CharField(default='Customer Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='description',
            field=models.TextField(default='Description', max_length=500),
        ),
        migrations.AlterField(
            model_name='quote',
            name='duty_percent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='image_url',
            field=models.URLField(default='http://www.example.com'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='imprint_cost',
            field=models.DecimalField(decimal_places=2, default=0.05, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='imprint_dimension',
            field=models.CharField(default='Imprint Dimension', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='imprint_location',
            field=models.CharField(default='Imprint Location', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='imprint_method',
            field=models.CharField(default='Imprint Method', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='moq',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='name',
            field=models.CharField(default='Product Name', max_length=150),
        ),
        migrations.AlterField(
            model_name='quote',
            name='ocean_freight',
            field=models.TextField(default='Ocean Freight', max_length=500),
        ),
        migrations.AlterField(
            model_name='quote',
            name='package',
            field=models.CharField(default='White Box', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='production_time',
            field=models.CharField(default='MUST BE SPECIFIED', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty1_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty1_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty2_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty2_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty3_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty3_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty4_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty4_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty5_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qty5_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quantity1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quantity2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quantity3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quantity4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quantity5',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quote',
            name='sales_rep',
            field=models.CharField(default='Sales Rep', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='tariff_percent',
            field=models.DecimalField(decimal_places=2, default=25.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='quote',
            name='vendor',
            field=models.CharField(default='Vendor Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='vendor_part_number',
            field=models.CharField(default='Vendor Part Number', max_length=50),
        ),
    ]

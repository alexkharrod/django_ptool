# Generated by Django 4.2.18 on 2025-01-26 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_air_freight_product_ocean_freight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(default='Complete', max_length=50),
            preserve_default=False,
        ),
    ]

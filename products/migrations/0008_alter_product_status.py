from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_product_colors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("Open", "Open"),
                    ("Added", "Added"),
                    ("Canceled", "Canceled"),
                ],
                default="Open",
                max_length=50,
            ),
        ),
    ]

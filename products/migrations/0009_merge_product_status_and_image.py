from django.db import migrations


class Migration(migrations.Migration):
    """Merge migration: combines 0008_alter_product_status and 0008_product_image."""

    dependencies = [
        ("products", "0008_alter_product_status"),
        ("products", "0008_product_image"),
    ]

    operations = []

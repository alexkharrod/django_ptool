from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Prospect",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("show_name", models.CharField(max_length=150)),
                ("show_date", models.DateField(blank=True, null=True)),
                ("vendor_name", models.CharField(max_length=150)),
                ("vendor_contact", models.CharField(blank=True, max_length=150)),
                ("vendor_email", models.CharField(blank=True, max_length=150)),
                ("vendor_website", models.CharField(blank=True, max_length=200)),
                ("product_name", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True, max_length=500)),
                (
                    "unit_cost",
                    models.CharField(
                        blank=True,
                        help_text='e.g. "$2.50 @ 500 pcs"',
                        max_length=100,
                    ),
                ),
                ("colors", models.CharField(blank=True, max_length=200)),
                ("lead_time", models.CharField(blank=True, max_length=100)),
                ("notes", models.TextField(blank=True, max_length=500)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="scouting/"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Spotted", "Spotted"),
                            ("Sample Ordered", "Sample Ordered"),
                            ("Evaluating", "Evaluating"),
                            ("Adding", "Adding"),
                            ("Rejected", "Rejected"),
                        ],
                        default="Spotted",
                        max_length=50,
                    ),
                ),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("promoted", models.BooleanField(default=False)),
                ("promoted_sku", models.CharField(blank=True, max_length=20)),
            ],
            options={
                "ordering": ["-date_added"],
            },
        ),
    ]

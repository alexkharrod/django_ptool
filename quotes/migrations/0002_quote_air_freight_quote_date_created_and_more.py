# Generated by Django 4.2.18 on 2025-01-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="quote",
            name="air_freight",
            field=models.TextField(default="0", max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="quote",
            name="date_created",
            field=models.DateTimeField(
                auto_now_add=True,
                default="2024-01-26 14:30:45.123456+0000",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="quote",
            name="ocean_freight",
            field=models.TextField(default="0", max_length=500),
            preserve_default=False,
        ),
    ]

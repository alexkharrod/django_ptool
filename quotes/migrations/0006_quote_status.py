# Generated by Django 4.2.18 on 2025-02-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_alter_quote_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='status',
            field=models.CharField(default='Quote Status', max_length=50),
        ),
    ]

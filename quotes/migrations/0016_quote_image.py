from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0015_alter_quote_reciprocal_tariffs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="image_url",
            field=models.CharField(blank=True, default="", max_length=2083),
        ),
        migrations.AddField(
            model_name="quote",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="quotes/"),
        ),
    ]

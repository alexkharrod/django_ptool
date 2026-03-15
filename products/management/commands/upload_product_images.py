"""
Management command: upload_product_images
-----------------------------------------
Reads each Product's legacy `image_url` filename (e.g. "EB59.jpg"),
opens the file from static/images/, and saves it into the new
`image` ImageField — which routes the file to Cloudinary when
CLOUDINARY_URL is configured, or local media/ in development.

Usage:
    python manage.py upload_product_images           # all products
    python manage.py upload_product_images --sku EB59 LY1302
    python manage.py upload_product_images --dry-run
"""

import os

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):
    help = "Upload existing static product images to Cloudinary (or media/) via the image ImageField."

    def add_arguments(self, parser):
        parser.add_argument(
            "--sku",
            nargs="+",
            help="Only process these SKUs (space-separated). Default: all products.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print what would happen without actually saving.",
        )
        parser.add_argument(
            "--skip-existing",
            action="store_true",
            default=True,
            help="Skip products that already have an image set (default: True).",
        )
        parser.add_argument(
            "--overwrite",
            action="store_true",
            help="Re-upload even if product.image is already set.",
        )

    def handle(self, *args, **options):
        static_images_dir = os.path.join(settings.BASE_DIR, "static", "images")
        dry_run = options["dry_run"]
        overwrite = options["overwrite"]

        qs = Product.objects.all()
        if options["sku"]:
            qs = qs.filter(sku__in=options["sku"])

        self.stdout.write(f"Found {qs.count()} product(s) to process.")
        ok = skipped = missing = already_done = 0

        for product in qs.order_by("sku"):
            filename = (product.image_url or "").strip()

            # Skip if already uploaded (unless --overwrite)
            if product.image and not overwrite:
                self.stdout.write(
                    self.style.WARNING(
                        f"  SKIP  {product.sku}: image already set to '{product.image.name}'"
                    )
                )
                already_done += 1
                continue

            if not filename:
                self.stdout.write(
                    self.style.WARNING(f"  SKIP  {product.sku}: no image_url value")
                )
                skipped += 1
                continue

            image_path = os.path.join(static_images_dir, filename)
            if not os.path.isfile(image_path):
                self.stdout.write(
                    self.style.ERROR(
                        f"  MISS  {product.sku}: file not found — {image_path}"
                    )
                )
                missing += 1
                continue

            if dry_run:
                self.stdout.write(f"  DRY   {product.sku}: would upload '{filename}'")
                ok += 1
                continue

            # Skip non-image files (e.g. PDFs accidentally stored as image_url)
            ext = os.path.splitext(filename)[1].lower()
            if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"):
                self.stdout.write(
                    self.style.WARNING(
                        f"  SKIP  {product.sku}: '{filename}' is not an image file"
                    )
                )
                skipped += 1
                continue

            # Read file and upload to Cloudinary via the ImageField
            with open(image_path, "rb") as f:
                data = f.read()

            # Upload to Cloudinary storage (save=False so compress_image in model.save() is NOT triggered)
            product.image.save(filename, ContentFile(data), save=False)
            # Use queryset .update() to write the image name directly to the DB,
            # bypassing the model's save() override (which would try to re-download
            # the file from Cloudinary for compression — causing a 401 error).
            Product.objects.filter(pk=product.pk).update(image=product.image.name)

            self.stdout.write(
                self.style.SUCCESS(
                    f"  OK    {product.sku}: uploaded as '{product.image.name}'"
                )
            )
            ok += 1

        self.stdout.write("")
        self.stdout.write(
            f"Done. OK={ok}  already_set={already_done}  skipped={skipped}  missing={missing}"
        )
        if dry_run:
            self.stdout.write(self.style.WARNING("(dry-run — nothing was saved)"))

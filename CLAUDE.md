# ptool — LogoIncluded Internal Product Tool

Built and maintained by Alex (President, LogoIncluded) with Claude.
This is an internal Django web app for managing promotional products, quotes, and scouting new items.

---

## What this tool does

### Products (`/products/`)
Full product catalog for LogoIncluded's line. Each product has SKU, specs, carton info, imprint details, freight/tariff costs, and an image. From a product page you can download a **NPDS (New Product Data Sheet)** as a PDF.

### Quotes (`/quotes/`)
Customer quote builder. Each quote has pricing at up to 5 quantity levels, air and ocean freight options, and can be downloaded as a **PDF**. Alex is not fully happy with the current quote system and plans to redesign it eventually.

### Scouting / Prospective Products (`/scouting/`)
Tool for tracking products spotted at trade shows. Alex uses this to photograph and log potential new items from vendor booths. Each prospect has vendor info, unit cost, lead time, notes, and a photo. When a prospect gets approved it can be promoted to a full Product.

**This is the preferred workflow for adding new products:**
1. Add a prospect via the scouting tool (photo uploads work automatically)
2. Review and evaluate
3. Promote to a full Product record when ready

---

## Deployment

- **Production**: Railway.app — auto-deploys on push to `main`
- **Database**: Railway PostgreSQL (shared between local dev and production)
- **Image storage**: Cloudinary — all product and quote images upload there automatically via `ImageField`
- **Static files**: served via `whitenoise` from `staticfiles/`
- **PDF generation**: WeasyPrint (lazy-imported to avoid startup crashes)

### Local development
Requires a `.env` file in the project root (never committed — in `.gitignore`):
```
SECRET_KEY=...
DEBUG=True
DATABASE_URL="postgresql://postgres:PASSWORD@interchange.proxy.rlwy.net:PORT/railway"
CLOUDINARY_URL="cloudinary://API_KEY:API_SECRET@CLOUD_NAME"
```
With `DATABASE_URL` set, local and Railway share the same Postgres database — changes made locally appear on Railway immediately.

---

## Image storage

Products and quotes use `ImageField` (upload_to `products/` and `quotes/` respectively). Images are:
- Automatically compressed and resized to max 800px wide on upload (via `compress_image()` in each model's `save()`)
- Stored on Cloudinary in production
- Old `image_url` CharField kept on both models as a fallback for any records not yet migrated

### Bulk upload legacy images
If you ever need to re-run the legacy image migration (static/images → Cloudinary):
```bash
DATABASE_URL="..." CLOUDINARY_URL="..." python manage.py upload_product_images
# Add --dry-run to preview, --sku EB59 LY1302 to target specific SKUs
```

---

## Key files

| File | Purpose |
|------|---------|
| `mysite/settings.py` | Main settings — DB, Cloudinary, static files all configured here |
| `products/models.py` | Product model with compress_image and ImageField |
| `quotes/models.py` | Quote model with compress_image and ImageField |
| `scouting/models.py` | Prospect model — the reference implementation for image upload pattern |
| `products/views.py` | Includes `npds()` — PDF datasheet download |
| `quotes/views.py` | Includes `quote_pdf()` — quote PDF download |
| `products/management/commands/upload_product_images.py` | One-time bulk upload of legacy static images to Cloudinary |
| `Dockerfile` | Railway build — Debian Bookworm base for WeasyPrint system libs |

---

## Known issues / backlog
- 3 products still have no image (find them by browsing products list — no image shown)
- Quote system is functional but Alex plans to redesign it
- `newsku` and `newskuaa` are test/placeholder SKUs that can be deleted

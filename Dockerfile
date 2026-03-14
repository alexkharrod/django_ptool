FROM python:3.13-slim-bookworm

# Install system dependencies required by WeasyPrint
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libcairo2 \
    libharfbuzz0b \
    fontconfig \
    libfreetype6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python manage.py collectstatic --noinput && python manage.py migrate && (python manage.py createsuperuser --noinput || true) && gunicorn mysite.wsgi --log-file - --workers 2 --bind 0.0.0.0:$PORT

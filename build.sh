#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install Node.js dependencies and build Tailwind CSS
if [ -f "package.json" ]; then
    npm install
    npm run build:css || npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --minify
fi

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Compress static files if django-compressor is installed
if pip freeze | grep -q django-compressor; then
    python manage.py compress
fi

# Create superuser if environment variables are set
if [[ -n "$DJANGO_SUPERUSER_USERNAME" ]] && [[ -n "$DJANGO_SUPERUSER_PASSWORD" ]] && [[ -n "$DJANGO_SUPERUSER_EMAIL" ]]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput
fi
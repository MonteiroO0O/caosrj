#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# LINHA NOVA PARA CRIAR O ADMIN AUTOMÁTICO
python create_admin.py
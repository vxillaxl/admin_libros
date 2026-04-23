#!/usr/bin/env bash
# Render: comando de compilación (Linux)
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --noinput

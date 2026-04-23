"""
Django settings for admin_libros project.
"""

from pathlib import Path
import os

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "dev-only-change-me-in-production-unsafe-key-12345",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() in ("1", "true", "yes")

_allowed_raw = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1")
ALLOWED_HOSTS = [h.strip() for h in _allowed_raw.split(",") if h.strip()]

# Render inyecta RENDER=true y RENDER_EXTERNAL_HOSTNAME (ej. admin-libros.onrender.com).
if os.environ.get("RENDER"):
    _ext = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "").strip()
    if _ext and _ext not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(_ext)
    # Permite el subdominio del servicio sin copiar/pegar en variables cada vez.
    if ".onrender.com" not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(".onrender.com")

ALLOWED_HOSTS = list(dict.fromkeys(ALLOWED_HOSTS))

_csrf_raw = os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "")
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _csrf_raw.split(",") if o.strip()]

if os.environ.get("RENDER"):
    _ext = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "").strip()
    if _ext:
        _origin = f"https://{_ext}"
        if _origin not in CSRF_TRUSTED_ORIGINS:
            CSRF_TRUSTED_ORIGINS.append(_origin)

CSRF_TRUSTED_ORIGINS = list(dict.fromkeys(CSRF_TRUSTED_ORIGINS))

# Render y otros proxies HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "gestion",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "admin_libros.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "admin_libros.wsgi.application"

# Local: SQLite. Producción (Render): variable DATABASE_URL al vincular PostgreSQL.
_sqlite_default = "sqlite:///" + (BASE_DIR / "db.sqlite3").resolve().as_posix()
DATABASES = {
    "default": dj_database_url.config(
        default=_sqlite_default,
        conn_max_age=600,
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "es"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

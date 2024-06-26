import datetime
import os
import sys
from pathlib import Path

import environ

from .common import *

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# env settings

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(str, "127.0.0.1 localhost"),
)

env.read_env(env.str("ENV_PATH", ".env"))

DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split()
SECRET_KEY = env("SECRET_KEY")

CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS").split()

# -----------------------------------------------------------------------------
# JSON Web Token (JWT)
# https://datatracker.ietf.org/doc/html/rfc7519
# -----------------------------------------------------------------------------
JWT_ACCESS_SECRET = env("JWT_ACCESS_SECRET")
JWT_REFRESH_SECRET = env("JWT_REFRESH_SECRET")
JWT_ACCESS_TOKEN_LIFETIME = datetime.timedelta(minutes=int(env("JWT_ACCESS_TOKEN_LIFETIME")))
JWT_REFRESH_TOKEN_LIFETIME = datetime.timedelta(days=int(env("JWT_REFRESH_TOKEN_LIFETIME")))

# -----------------------------------------------------------------------------
# Yoomoney integration
# https://yoomoney.ru/about
# -----------------------------------------------------------------------------
YOOMONEY_TOKEN = env("YOOMONEY_TOKEN")
RECIPIENT_ACCOUNT = env("RECIPIENT_ACCOUNT")
SUBSCRIPTION_COST = 2 # Two rubles
MINIMUM_PAYMENT = 1.9

# -----------------------------------------------------------------------------
# DATABASES - PostgreSQL
# -----------------------------------------------------------------------------
DATABASES["default"].update(
    ENGINE=env("DB_ENGINE"),
    NAME=env("POSTGRES_NAME"),
    USER=env("POSTGRES_USER"),
    PASSWORD=env("POSTGRES_PASSWORD"),
    HOST=env("POSTGRES_HOST"),
    PORT=env("POSTGRES_PORT"),
)

# -----------------------------------------------------------------------------
# CELERY
# -----------------------------------------------------------------------------
redis_host = env.str("REDIS_HOST")
redis_port = env.int("REDIS_PORT")
redis_db = env.int("REDIS_DB")

CELERY_BROKER_URL = f"redis://{redis_host}:{redis_port}/{redis_db}"
CELERY_RESULT_BACKEND = f"redis://{redis_host}:{redis_port}/{redis_db}"

DEFAULT_CHARSET = "utf-8"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "static"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

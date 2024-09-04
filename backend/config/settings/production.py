from config.settings.base import *
from decouple import config

DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOSTNAME", "localhost"),
        "NAME": os.getenv("DB_NAME", "name"),
        "USER": os.getenv("DB_USERNAME", "username"),
        "PASSWORD": os.getenv("DB_PASSWORD", "password"),
        "PORT": int(os.getenv("DB_PORT", "5432")),
        "OPTIONS": {
            "pool": {
                "min_size": 2,
                "max_size": 20,
                "timeout": 30,
            },
        },
    },
}
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../", "staticfiles")  # type: ignore

# settings.py
import sentry_sdk


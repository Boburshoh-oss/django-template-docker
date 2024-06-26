from config.settings.base import *
from decouple import config

DEBUG = False

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../", "staticfiles")  # type: ignore

# settings.py
import sentry_sdk


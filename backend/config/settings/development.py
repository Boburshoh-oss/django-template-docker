from config.settings.base import *
import os
import mimetypes

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOSTNAME", "db"),
        "NAME": os.environ.get("DB_NAME", "postgres"),
        "USER": os.environ.get("DB_USERNAME", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "postgres"),
        "PORT": int(os.environ.get("DB_PORT", "5432")),
    }
}
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../", "staticfiles")

INTERNAL_IPS = [
    "127.0.0.1",
    "0.0.0.0",
]


mimetypes.add_type("application/javascript", ".js", True)

DEBUG_TOOLBAR_PATCH_SETTINGS = False


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    'INSERT_BEFORE': '</head>',
    'RENDER_PANELS': True,
}
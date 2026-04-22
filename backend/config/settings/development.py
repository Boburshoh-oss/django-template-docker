from config.settings.base import *  # noqa: F403
import mimetypes

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOSTNAME", "db"),
        "NAME": os.getenv("DB_NAME", "postgres"),
        "USER": os.getenv("DB_USERNAME", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
        "PORT": int(os.getenv("DB_PORT", "5432")),
    }
}

STATIC_ROOT = BASE_DIR / "../staticfiles"

INTERNAL_IPS = ["127.0.0.1", "0.0.0.0"] + env_list("INTERNAL_IPS", [])

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


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
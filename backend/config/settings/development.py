from config.settings.base import *
import os
import mimetypes

DEBUG = True

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
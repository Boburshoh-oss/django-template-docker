from config.settings.base import *

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
SECURE_SSL_REDIRECT = env_bool("SECURE_SSL_REDIRECT", False)
SESSION_COOKIE_SECURE = env_bool("SESSION_COOKIE_SECURE", SECURE_SSL_REDIRECT)
CSRF_COOKIE_SECURE = env_bool("CSRF_COOKIE_SECURE", SECURE_SSL_REDIRECT)
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", 0))
SECURE_HSTS_INCLUDE_SUBDOMAINS = env_bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", False)
SECURE_HSTS_PRELOAD = env_bool("SECURE_HSTS_PRELOAD", False)

import sentry_sdk


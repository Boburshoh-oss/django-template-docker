import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "drf_yasg",
    "corsheaders",
    "django_filters",
    "debug_toolbar",
    # for seo
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "drf_standardized_errors",
    # my apps
    # 'apps.managers',
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # YENİ
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # 'debug_toolbar.middleware.show_toolbar'
]

# redis settings
LOCATION_REDIS = os.getenv("REDIS_URL", "redis://redis:6379") + "/1"
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": LOCATION_REDIS,
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "mane",
    }
}

REDIS_TIMEOUT = int(os.getenv("REDIS_TIMEOUT", 300))

CSRF_TRUSTED_ORIGINS = [
    "http://0.0.0.0:8000/",
    "http://0.0.0.0",
    "http://localhost",
    "https://manecafe.uz",
    "https://api.manecafe.uz/",
    "https://api.manecafe.uz",
    "https://manecafe.uz/",
]
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = "*"
DOMAIN_NAME = os.environ.get("DOMAIN_NAME", "https://api.manecafe.uz")
# DOMAIN_NAME = "https://1fda-188-113-213-235.ngrok-free.app"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "../templates", os.path.join(BASE_DIR, "../templates")],
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

# WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

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

FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # (50MEGABYTES)
DATA_UPLOAD_MAX_MEMORY_SIZE = FILE_UPLOAD_MAX_MEMORY_SIZE

# DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
# maximal vide hajmini limiti

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.IsAuthenticated",
    # ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 40,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    # 'EXCEPTION_HANDLER': 'apps.utils.custom_exception.custom_exception_handler'
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}
DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}

LANGUAGE_CODE = "uz"

USE_L10N = True

USE_I18N = True

USE_TZ = True
TIME_ZONE = "Asia/Tashkent"

# LANGUAGES = (("en", "English"), ("ru", "Russian"), ("uz", "Uzbek"))
gettext = lambda s: s
LANGUAGES = (
    ("uz", gettext("Uzbek")),
    ("ru", gettext("Russian")),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"
MODELTRANSLATION_LANGUAGES = ("uz", "ru")

LOCALE_PATHS = [
    BASE_DIR / "locale/",
]

STATIC_URL = "static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "../", "media/")

# celery broker and result
CELERY_BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("RESULT_BACKEND", "redis://localhost:6379/0")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REVERSION = {
    "DELETE_STALE_VERSIONS": False,
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=28),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# swagger
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "basic": {"type": "basic"},
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, "
            "where JWT is the JSON web token you get back when logging in.",
        },
    }
}

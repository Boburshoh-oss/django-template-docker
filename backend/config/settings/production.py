from config.settings.base import *
from decouple import config

DEBUG = False

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../", "staticfiles")  # type: ignore

# settings.py
import sentry_sdk

# sentry_sdk.init(
#     dsn="https://d4f5fea8d87dfdf5f68f6abb898e2651@o4506259320274944.ingest.us.sentry.io/4507021769048064",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )

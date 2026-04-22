import logging

from django.conf import settings
from django.db import connection

logger = logging.getLogger(__name__)

_QUERY_WARN_THRESHOLD = int(getattr(settings, "QUERY_WARN_THRESHOLD", 20))
_QUERY_TIME_THRESHOLD = float(getattr(settings, "QUERY_TIME_THRESHOLD", 0.5))


class QueryCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if settings.DEBUG:
            count = len(connection.queries)
            total_time = sum(float(q["time"]) for q in connection.queries)

            if count > _QUERY_WARN_THRESHOLD:
                logger.warning(
                    "High query count: %d queries on %s %s",
                    count,
                    request.method,
                    request.path,
                )
            if total_time > _QUERY_TIME_THRESHOLD:
                logger.warning(
                    "Slow queries: %.3fs total on %s %s",
                    total_time,
                    request.method,
                    request.path,
                )

        return response
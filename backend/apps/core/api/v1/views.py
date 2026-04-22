from django.core.cache import cache
from django.db import connection
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(exclude=True)
    def get(self, request):
        health = {"status": "ok", "db": False, "cache": False}

        try:
            connection.ensure_connection()
            health["db"] = True
        except Exception:
            health["status"] = "degraded"

        try:
            cache.set("health_check", "1", timeout=5)
            health["cache"] = cache.get("health_check") == "1"
        except Exception:
            health["status"] = "degraded"

        status_code = 200 if health["status"] == "ok" else 503
        return Response(health, status=status_code)

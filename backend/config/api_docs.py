from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

api_docs_urlpatterns = [
    SpectacularAPIView.as_view(
        authentication_classes=[],
        permission_classes=[],
    ),
    SpectacularSwaggerView.as_view(
        url_name="schema",
        authentication_classes=[],
        permission_classes=[],
    ),
    SpectacularRedocView.as_view(
        url_name="schema",
        authentication_classes=[],
        permission_classes=[],
    ),
]

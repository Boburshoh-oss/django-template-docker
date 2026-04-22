from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.api_docs import api_docs_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.routers.v1")),
    *api_docs_urlpatterns,
]

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    try:
        import debug_toolbar  # noqa: F401
        urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    except ImportError:
        pass

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

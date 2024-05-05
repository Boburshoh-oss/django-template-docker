from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from .scheme import swagger_urlpatterns


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),

    path('api/v1/', include('apps.urls')),

    path("__debug__/", include("debug_toolbar.urls")),

]
urlpatterns += swagger_urlpatterns

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

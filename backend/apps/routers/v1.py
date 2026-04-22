from django.urls import include, path

urlpatterns = [
    path("health/", include("apps.core.api.v1.urls")),
    path("accounts/", include("apps.accounts.api.v1.urls")),
]

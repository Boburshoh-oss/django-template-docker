from django.urls import path

from .views import MeView

urlpatterns = [
    path("me/", MeView.as_view(), name="accounts-me"),
]

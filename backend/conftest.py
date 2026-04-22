import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def auth_client(api_client, django_user_model):
    user = django_user_model.objects.create_user(
        phone_number="+998900000000",
        password="testpass123",
    )
    api_client.force_authenticate(user=user)
    return api_client, user

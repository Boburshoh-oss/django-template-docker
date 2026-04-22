import pytest


@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self, django_user_model):
        user = django_user_model.objects.create_user(
            phone_number="+998901234567",
            password="testpass123",
        )
        assert user.phone_number == "+998901234567"
        assert user.check_password("testpass123")
        assert not user.is_staff

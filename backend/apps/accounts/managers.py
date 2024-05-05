import re
from django.contrib.auth.base_user import BaseUserManager


def is_phone_number(phone: str) -> bool:
    pattern = r"^(?:\+998|998|)([1-9]\d{8})$"
    match = re.match(pattern, phone)
    if match:
        return True
    else:
        return False


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")
        if not is_phone_number(phone_number):
            raise ValueError("Telefon raqam to'g'ri kiriting!")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(phone_number, password, **extra_fields)

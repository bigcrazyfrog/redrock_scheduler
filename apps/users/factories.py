import uuid

from django.conf import settings

import factory

from . import models

DEFAULT_PASSWORD = "Test111!"


class UserFactory(factory.django.DjangoModelFactory):
    """Factory to generate test User instance."""

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall(
        "set_password",
        DEFAULT_PASSWORD,
    )

    class Meta:
        model = models.User

    @factory.lazy_attribute
    def email(self) -> str:
        """Return formatted email."""
        return (
            f"{uuid.uuid4()}@"
            f"{settings.APP_LABEL.lower().replace(' ', '-')}.com"
        )


class AdminUserFactory(UserFactory):
    """Factory to generate test User model with admin's privileges."""

    is_superuser = True
    is_staff = True
    is_premium = True

    class Meta:
        model = models.User


class PremiumUserFactory(UserFactory):
    """Factory to generate test User model with premium's privileges."""

    is_premium = True

    class Meta:
        model = models.User

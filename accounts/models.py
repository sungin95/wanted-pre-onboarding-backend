from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ParseError


class User(AbstractUser):
    # unique=True를 위해 재정의
    email = models.CharField(
        _("email address"),
        max_length=50,
        unique=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        email = kwargs.get("email")
        if email and email.find("@") == -1:
            raise ParseError

        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.username

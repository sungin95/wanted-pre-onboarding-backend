from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import NotFound
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
        if email:
            User.email_check(kwargs["email"])

        super().__init__(*args, **kwargs)

    def email_check(email: str):
        if email.find("@") == -1:
            raise ParseError

    def __str__(self):
        return self.username

    def get_object(pk: int):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def create_test_list(n: int) -> list:
        user_list = []
        for i in range(n):
            id_ = "testuser" + str(i)
            user = User.objects.create(
                username=id_,
                email=id_ + "@naver.com",
            )
            user.set_password("123")
            user.save()
            user_list.append(user)
        return user_list

    def email_to_username(email: str):
        username = email.split("@")[0]
        if username:
            return username
        # 아무것도 없으면 오류
        else:
            raise ParseError

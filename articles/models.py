from django.db import models
from common.models import CommonModel
from accounts.models import User
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ParseError


class Articles(CommonModel):
    owner = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
    )
    context = models.TextField()

    # 모델 관리
    def get_object(pk: int):
        try:
            return Articles.objects.get(pk=pk)
        except Articles.DoesNotExist:
            raise NotFound

    def create_test_list(n: int, user: User) -> list:
        articles_list = []
        for _ in range(n):
            article = Articles.objects.create(
                title="test title",
                context="test context",
                owner=user,
            )
            articles_list.append(article)
        return articles_list

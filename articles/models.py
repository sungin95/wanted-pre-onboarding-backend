from django.db import models
from common.models import CommonModel
from accounts.models import User
from rest_framework.exceptions import NotFound
from django.db import transaction
from rest_framework.exceptions import ParseError


# 공용 질문
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

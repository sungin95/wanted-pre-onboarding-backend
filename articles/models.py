from django.db import models
from common.models import CommonModel


class Articles(CommonModel):
    owner = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
    )
    context = models.TextField()

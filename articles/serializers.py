from rest_framework.serializers import ModelSerializer
from .models import Articles


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            "pk",
            "title",
            "context",
        )

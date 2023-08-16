from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    ParseError,
    PermissionDenied,
    NotFound,
    NotAuthenticated,
)
from rest_framework import status
from .models import Articles
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from config import settings


def page_nation(page_size, page):
    try:
        page = int(page)
    except ValueError:
        page = 1
    page_size = page_size
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class ArticleGetCreate(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        page = request.GET.get("page", None)
        if page is None:
            page = 1
        (start, end) = page_nation(settings.PAGE_SIZE, page)
        all_articles = Articles.objects.all()[start:end]
        serializer = ArticleSerializer(
            all_articles,
            many=True,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        articleSerializer = ArticleSerializer(
            data=request.data,
        )
        if articleSerializer.is_valid():
            articleSerializer.save(
                owner=request.user,
            )
            return Response(
                articleSerializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            articleSerializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


from accounts.models import User


def user_not_equal(request_user: User, user: User) -> bool:
    if request_user != user:
        return True
    else:
        return False


class ArticleDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, article_pk):
        article = Articles.get_object(article_pk)
        serializer = ArticleSerializer(article)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, article_pk):
        article = Articles.get_object(article_pk)
        if user_not_equal(request.user, article.owner):
            raise PermissionDenied
        serializer = ArticleSerializer(
            article,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, article_pk):
        article = Articles.get_object(article_pk)
        if user_not_equal(request.user, article.owner):
            raise PermissionDenied
        article.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

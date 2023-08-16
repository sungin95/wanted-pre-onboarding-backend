from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    PermissionDenied,
)
from rest_framework import status
from .models import Articles
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from .serializers import ArticleSerializer
from rest_framework import status
from config import settings
from functions.articles import page_nation, article_get_object
from functions.accounts import user_not_equal


class ArticleGetCreate(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # 쿼리매개 변수를 통해 page정보를 줘야 합니다.(?page=2)
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


class ArticleDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, article_pk):
        article = article_get_object(article_pk)
        serializer = ArticleSerializer(article)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, article_pk):
        article = article_get_object(article_pk)
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
        article = article_get_object(article_pk)
        if user_not_equal(request.user, article.owner):
            raise PermissionDenied
        article.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )

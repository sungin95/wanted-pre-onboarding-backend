from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleGetCreate.as_view()),
    path("detail/<int:article_pk>", views.ArticleDetail.as_view()),
]

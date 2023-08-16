from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleGetCreate.as_view()),
    path("detail", views.ArticleDetail.as_view()),
]

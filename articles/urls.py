from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleGetCreate.as_view()),
    # path("log-in", views.LogIn.as_view()),
]

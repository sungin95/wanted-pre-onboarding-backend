from django.urls import path
from . import views

urlpatterns = [
    path("create", views.UserCreate.as_view()),
    path("log-in", views.LogIn.as_view()),
]

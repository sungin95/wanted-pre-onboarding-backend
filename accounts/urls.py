from django.urls import path
from . import views

urlpatterns = [
    path("create", views.UserGetCreate.as_view()),
]

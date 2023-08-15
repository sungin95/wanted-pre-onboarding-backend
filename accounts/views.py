from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    PermissionDenied,
    ParseError,
    NotFound,
    NotAuthenticated,
    ParseError,
)
from rest_framework import status
from .models import User
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from config import settings


class UserCreate(APIView):
    def get(self, request):
        return Response(
            {"ok": "ok"},
            status.HTTP_201_CREATED,
        )

    def post(self, request):
        print(123)
        return Response(
            {"ok": "ok"},
            status.HTTP_201_CREATED,
        )

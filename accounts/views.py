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


class UserGetCreate(APIView):
    def get(self, request):
        return Response(status.HTTP_200_OK)

    def post(self, request):
        return Response(status.HTTP_201_CREATED)

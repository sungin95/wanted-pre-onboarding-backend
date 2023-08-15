from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    ParseError,
    PermissionDenied,
    NotFound,
    NotAuthenticated,
)
from rest_framework import status
from .models import User
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
    BasePermission,
)
from config import settings
from .serializers import UserCreateSerializer
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreate(APIView):
    permission_classes = [BasePermission]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password or len(password) < 8:
            raise ParseError
        serializer = UserCreateSerializer(
            data={
                "email": email,
            },
        )
        if serializer.is_valid():
            user = serializer.save(
                username=User.email_to_username(email),
            )
            user.set_password(password)
            user.save()
            # 토큰
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "회원가입 완료",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status.HTTP_201_CREATED,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        return Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST,
        )

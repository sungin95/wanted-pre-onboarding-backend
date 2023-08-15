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
from .serializers import UserSerializer
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login, logout


class UserCreate(APIView):
    permission_classes = [BasePermission]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password or len(password) < 8:
            raise ParseError
        serializer = UserSerializer(
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


class LogIn(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            raise ParseError
        user = authenticate(
            email=email,
            password=password,
        )
        if user is not None:
            serializer = UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": f"{user.username}님 환영합니다.",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res

        else:
            return Response(
                {"errors": "아이디 혹은 비밀번호가 잘못되었습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"ok": "bye!"},
            status=status.HTTP_200_OK,
        )

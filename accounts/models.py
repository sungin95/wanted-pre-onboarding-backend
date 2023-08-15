from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from common.models import CommonModel
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, CommonModel):
    # DB에 저장할 데이터를 선언
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    email = models.EmailField(
        "이메일 주소",
        max_length=50,
        unique=True,
    )
    fullname = models.CharField(
        "이름",
        max_length=20,
        blank=True,
        null=True,
    )

    # 활성화 여부 (기본값은 True)
    is_active = models.BooleanField(default=True)

    # 관리자 권한 여부 (기본값은 False)
    is_admin = models.BooleanField(default=False)

    # 실제 로그인에 사용되는 아이디
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    # custom user 생성 시 필요
    objects = UserManager()

    # 어드민 페이지에서 데이터를 제목을 어떻게 붙여줄 것인지 지정
    def __Str__(self):
        return f"{self.username} / {self.email} 님의 계정입니다"

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    # 일반적으로 선언만 해두고 건들지않는다
    def has_perm(self, perm, obj=None):
        return True

    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    # 일반적으로 선언만 해두고 건들지않는다
    def has_module_perms(self, app_label):
        return True

    # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin


# def create(self, validation_data):
#         password = validation_data.pop('password')
#         password = make_password(password)  # make_password(해시하고자 하는 변수)로 단 한줄로 끝!
#         validation_data['password'] = password

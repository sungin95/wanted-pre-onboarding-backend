from accounts.models import User
from rest_framework.exceptions import NotFound, ParseError


def user_not_equal(request_user: User, user: User) -> bool:
    if request_user != user:
        return True
    else:
        return False


def user_get_object(pk: int):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise NotFound


def email_to_username(email: str):
    username = email.split("@")[0]
    if username:
        return username
    # 아무것도 없으면 오류
    else:
        raise ParseError


def user_create_test_list(n: int) -> list:
    user_list = []
    for i in range(n):
        id_ = "testuser" + str(i)
        user = User.objects.create(
            username=id_,
            email=id_ + "@naver.com",
        )
        user.set_password("12345678")
        user.save()
        user_list.append(user)
    return user_list

from rest_framework.test import APITestCase
from accounts.models import User


class TestCreateUser(APITestCase):
    URL = "/api/v1/accounts/create"

    def setUp(self):
        user = User.objects.create(
            email="testuser@naver.com",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_user(self):
        print(self.user)

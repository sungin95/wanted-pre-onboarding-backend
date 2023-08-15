from rest_framework.test import APITestCase
from accounts.models import User


class TestCreateUser(APITestCase):
    URL = "/api/v1/accounts/create"

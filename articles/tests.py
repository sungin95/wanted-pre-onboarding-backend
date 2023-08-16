from rest_framework.test import APITestCase
from accounts.models import User
from .models import Articles
from config import settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TestArticlesGet(APITestCase):
    URL = "/api/v1/articles/"

    def setUp(self):
        self.articles_len = 12
        user_list = User.create_test_list(1)
        self.user = user_list[0]
        Articles.create_test_list(self.articles_len, self.user)
        self.TITLE = "test title"
        self.CONTENT = "test context"

    def test_Articles_GET_1(self):
        response = self.client.get(self.URL)
        self.assertEqual(
            response.status_code,
            200,
            "status code isn't 200.",
        )

    def test_Articles_GET_Pagenation_1(self):
        page = 3
        response = self.client.get(self.URL + "?page=" + str(page))
        data = response.json()
        get_article = self.articles_len - (settings.PAGE_SIZE * (page - 1))
        if 0 > get_article:
            get_article = 0
        elif get_article > settings.PAGE_SIZE:
            get_article = settings.PAGE_SIZE
        self.assertEqual(
            len(data),
            get_article,
            "status code isn't 200.",
        )


class TestArticlesCreateLogout(APITestCase):
    URL = "/api/v1/articles/"

    def setUp(self):
        user_list = User.create_test_list(1)
        self.user = user_list[0]

    def test_Articles_Create_1(self):
        response = self.client.post(
            self.URL,
            data={
                "title": "test title",
                "context": "test context",
            },
        )
        self.assertEqual(
            response.status_code,
            401,
            "status code isn't 401.",
        )


class TestArticlesCreateLogin(APITestCase):
    URL = "/api/v1/articles/"

    def setUp(self):
        user_list = User.create_test_list(1)
        self.user = user_list[0]
        token = TokenObtainPairSerializer.get_token(self.user)
        access_token = str(token.access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}",
        )

    def test_Articles_Create_1(self):
        response = self.client.post(
            self.URL,
            data={
                "title": "test title",
                "context": "test context",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "status code isn't 201.",
        )

    def test_Articles_Create_2(self):
        response = self.client.post(
            self.URL,
            data={
                "title": "test title",
                "context": "test context",
            },
        )
        data = response.json()
        self.assertEqual(
            data["title"],
            "test title",
            "제목이 잘못 저장되었습니다.",
        )

    def test_Articles_Create_3(self):
        response = self.client.post(
            self.URL,
            data={
                "title": "test title",
                "context": "test context",
            },
        )
        data = response.json()
        self.assertEqual(
            data["context"],
            "test context",
            "본문이 잘못 저장되었습니다.",
        )

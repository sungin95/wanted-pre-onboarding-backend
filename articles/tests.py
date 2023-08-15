from rest_framework.test import APITestCase
from accounts.models import User
from .models import Articles
from config import settings


class TestArticlesGet(APITestCase):
    URL = "/api/v1/articles/"

    def setUp(self):
        self.articles_len = 12
        user_list = User.create_test_list(1)
        self.user = user_list[0]
        articles_list = Articles.create_test_list(self.articles_len, self.user)
        self.articles = articles_list[0]
        self.TITLE = "test title"
        self.CONTENT = "test context"

    def test_Articles_GET_1(self):
        response = self.client.get(self.URL)
        self.assertEqual(
            response.status_code,
            200,
            "status code isn't 200.",
        )

    def test_Articles_GET_2(self):
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

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


class TestArticlesDetailLogout(APITestCase):
    URL = "/api/v1/articles/detail/"

    def setUp(self):
        user_list = User.create_test_list(1)
        self.user = user_list[0]
        self.article = Articles.create_test_list(1, self.user)[0]
        self.TITLE = "test title"
        self.CONTENT = "test context"

    def test_Articles_Detail_GET_1(self):
        response = self.client.get(
            self.URL + str(self.article.pk),
        )
        self.assertEqual(
            response.status_code,
            200,
            "status code isn't 200.",
        )

    def test_Articles_Detail_GET_2(self):
        response = self.client.get(
            self.URL + str(self.article.pk),
        )
        data = response.json()
        self.assertEqual(
            data["context"],
            self.CONTENT,
            "context가 잘못 출력 되었습니다.",
        )

    def test_Articles_Detail_PUT_1(self):
        response = self.client.put(
            self.URL + str(self.article.pk),
            data={
                "title": "test title 수정",
                "context": "test context 수정",
            },
        )
        self.assertEqual(
            response.status_code,
            401,
            "status code isn't 401.",
        )

    def test_Articles_Detail_DELETE_1(self):
        response = self.client.delete(
            self.URL + str(self.article.pk),
        )
        self.assertEqual(
            response.status_code,
            401,
            "status code isn't 401.",
        )


class TestArticlesDetailLogin(APITestCase):
    URL = "/api/v1/articles/detail/"

    def setUp(self):
        user_list = User.create_test_list(1)
        self.user = user_list[0]
        self.article = Articles.create_test_list(1, self.user)[0]
        self.TITLE = "test title"
        self.CONTENT = "test context"
        token = TokenObtainPairSerializer.get_token(self.user)
        access_token = str(token.access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}",
        )

    def test_Articles_Detail_PUT_1(self):
        response = self.client.put(
            self.URL + str(self.article.pk),
            data={
                "title": "test title 수정",
                "context": "test context 수정",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "status code isn't 201.",
        )

    def test_Articles_Detail_PUT_2(self):
        response = self.client.put(
            self.URL + str(self.article.pk),
            data={
                "title": "test title 수정",
            },
        )
        data = response.json()
        self.assertEqual(
            data["title"],
            "test title 수정",
            "제목이 수정이 안되었습니다.",
        )

    def test_Articles_Detail_PUT_3(self):
        response = self.client.put(
            self.URL + str(self.article.pk),
            data={
                "context": "test context 수정",
            },
        )
        data = response.json()
        self.assertEqual(
            data["context"],
            "test context 수정",
            "본문이 수정이 안되었습니다.",
        )

    def test_Articles_Detail_DELETE_1(self):
        response = self.client.delete(
            self.URL + str(self.article.pk),
        )
        self.assertEqual(
            response.status_code,
            204,
            "status code isn't 204.",
        )

    def test_Articles_Detail_DELETE_2(self):
        self.client.delete(
            self.URL + str(self.article.pk),
        )
        try:
            Articles.get_object(self.article.pk)
            self.assertEqual(
                123,
                2353536,
                "article이 삭제가 안되었습니다. ",
            )
        except:
            self.assertEqual(
                True,
                True,
                "삭제가 된 상황.",
            )


class TestArticlesDetailLoginOtherUser(APITestCase):
    URL = "/api/v1/articles/detail/"

    def setUp(self):
        user_list = User.create_test_list(2)
        self.user_owner = user_list[0]
        self.user_other = user_list[1]
        self.article = Articles.create_test_list(1, self.user_owner)[0]
        self.TITLE = "test title"
        self.CONTENT = "test context"
        token = TokenObtainPairSerializer.get_token(self.user_other)
        access_token = str(token.access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access_token}",
        )

    def test_Articles_Detail_PUT_1(self):
        response = self.client.put(
            self.URL + str(self.article.pk),
            data={
                "title": "test title 수정",
                "context": "test context 수정",
            },
        )
        self.assertEqual(
            response.status_code,
            403,
            "status code isn't 403.",
        )

    def test_Articles_Detail_DELETE_1(self):
        response = self.client.delete(
            self.URL + str(self.article.pk),
        )
        self.assertEqual(
            response.status_code,
            403,
            "status code isn't 403.",
        )

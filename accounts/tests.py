from rest_framework.test import APITestCase
from accounts.models import User


# 아이디 생성 테스트
class TestCreateUser(APITestCase):
    URL = "/api/v1/accounts/create"

    def test_create_user_1(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "testuser@naver.com",
                "password": "@As5121926",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "status code isn't 201.",
        )

    def test_create_user_2(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "testuser@naver.com",
                "password": "@As5121926",
            },
        )
        data = response.json()
        self.assertEqual(
            User.get_object(data["pk"]).email,
            "testuser@naver.com",
            "status code isn't 201.",
        )

    def test_create_user_3(self):
        try:
            response = self.client.post(
                self.URL,
                data={
                    "email": "testuser@naver.com",
                    "password": "1",
                },
            )
            self.assertEqual(
                False,
                "실패",
                "1자리는 생성 될 수 없습니다.",
            )
        except:
            self.assertEqual(
                True,
                True,
                "1자리는 오류가 걸려서 이게 실행 되어야 한다.",
            )

    def test_create_user_4(self):
        try:
            response = self.client.post(
                self.URL,
                data={
                    "email": "testuser@naver.com",
                    "password": "1234567",
                },
            )
            self.assertEqual(
                False,
                "실패",
                "7자리는 생성 될 수 없습니다.",
            )
        except:
            self.assertEqual(
                True,
                True,
                "7자리는 오류가 걸려서 이게 실행 되어야 한다.",
            )

    def test_create_user_5(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "testuser@naver.com",
                "password": "12345678",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "비밀번호 8자리가 생성이 안되었습니다. ",
        )

    def test_create_user_6(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "testuser@naver.com",
                "password": "!@#$%^&*",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "비밀번호 8자리가 생성이 안되었습니다. ",
        )

    def test_create_user_7(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "testuser@naver.com",
                "password": "abcdefgh",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "비밀번호 8자리가 생성이 안되었습니다. ",
        )

    # 이메일 검사
    def test_create_user_8(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "testuser",
                "password": "abcdefgh",
            },
        )
        self.assertEqual(
            response.status_code,
            400,
            "@가 없으면 생성이 되면 안됩니다. ",
        )

    def test_create_user_9(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "t@asd",
                "password": "abcdefgh",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "추가적인 유효성 검사 조건이 있습니다. ",
        )

    def test_create_user_10(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "t@@@asd",
                "password": "abcdefgh",
            },
        )
        self.assertEqual(
            response.status_code,
            201,
            "추가적인 유효성 검사 조건이 있습니다. ",
        )

    def test_create_user_11(self):
        response = self.client.post(
            self.URL,
            data={
                "email": "@@@asd",
                "password": "abcdefgh",
            },
        )

        self.assertEqual(
            response.status_code,
            400,
            "@로 시작하였습니다.",
        )


# 유저 중복 생성 테스트
class TestCreateUserDuplication(APITestCase):
    URL = "/api/v1/accounts/create"

    def setUp(self):
        user = User.create_test_list(1)[0]
        self.user = user

    def test_create_user_22(self):
        response = self.client.post(
            self.URL,
            data={
                "email": f"{self.user.email}",
                "password": "@As5121926",
            },
        )
        self.assertEqual(
            response.status_code,
            400,
            "status code isn't 400.",
        )

    def test_create_user_3(self):
        response = self.client.post(
            self.URL,
            data={
                "email": f"{self.user.email}",
                "password": "@As5121926",
            },
        )
        data = response.json()
        self.assertEqual(
            data["email"],
            ["user with this email address already exists."],
            "email 중복 생성되었습니다.",
        )

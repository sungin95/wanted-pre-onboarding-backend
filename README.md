# wanted-pre-onboarding-backend

백엔드 프리온보팅 인턴십 8월 사전 과제

성명: 이성인

애플리케이션의 실행 방법 (엔드포인트 호출 방법 포함)
[배포 주소](http://ec2-52-78-88-145.ap-northeast-2.compute.amazonaws.com/api/v1/articles/)
도메인 설계:
articles(게시판)
/api/v1/articles/?page=2
메서드: GET
페이지 네이션을 이용 게시판 조회

메서드: POST
게시판 생성
JWT토큰 필요
데이터 형식

```
{
    "title": xxx,
    "context": xxx
}
```

/api/v1/articles/detail/<article_pk>
메서드 GET
조회한 게시판 정보 조회

메서드 PUT
JWT토큰 필요
작성자여야 한다.
데이터를 보내면 수정

```
{
    "title": xxx,
    "context": xxx
}
```

메서드 DELETE
JWT토큰 필요
작성자여야 한다.
해당 게시물 삭제

accounts<유저>
/api/v1/accounts/create
메서드 POST
데이터를 보내면 유저 생성(자동 토큰 발행)

```
{
    "email": xxx@nab,
    "password": xxx
}
```

/api/v1/accounts/log-in
메서드 POST
데이터를 보내면 유저 로그인(토큰 발행)

```
{
    "email": xxx@nab,
    "password": xxx
}
```

데이터베이스 테이블 구조
[ERD](https://viewer.diagrams.net/?tags=%7B%7D&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=ERD.svg#R7VhrU6MwFP01nXE%2FuMNDav1YWqvrY9f342OEFLKGhE1SW%2Frr9wZCgeJq6%2Bg6Os50Bu7JTULuOYHTdNxBMtsTKI2PeYhpx7HCWccddhzHtnc8uGgkK5Cu6xRAJEhokirgnMyxAS2DTkiIZSNRcU4VSZtgwBnDgWpgSAg%2BbaaNOW3OmqIIt4DzANE2ek1CFRdoz9mu8H1Moric2e7uFC0JKpPNSmSMQj6tQe5uxx0IzlVxl8wGmOrilXW5%2FpFd06P77t7BqfyDLv3Di59Xm8Vgo3W6LJYgMFMvHnp%2BPx7tX239vklPRqdTa69%2Fd7BpulgPiE5MvS4lFma9KiuLKKckoYhB5I85U%2BemBUrgI0oiBvcBPBv0dP0HLBSB%2BvdNg%2BIpoEFMaHiEMj7RK5AKBfdl5MdckDkMiyg02QBAs1BGSk63kXGuewJsASqwhJyTsiz2AjpCUpmcgFOKUknu8gfWKQkSEWE%2BV4on5UB8wkIcmmjBcx4owe8XytH9VyTDkKargWc1KRpy9jBPsBIZpJjWhc7MRrPLeFrJ1u4aLG5I1oDIbJVoMfZiujPYWohFUIRqPndpvq0V5wNGGtMhCsQzpLCvyyjrIoSb2lIrKJfmGjK1WzKdSD1ngltShWqrmiwpHqt%2FilKmKCAsOspzhlsVcmZWqyEOfcc0F0RMwhCzXDAKKVRoSqsk5YSpvByeDz8o2sD67nU8eKABxHYVw0%2BnCzXgDLSFSC4iDIKdYi3aR%2BT15MZ9Xl5Zk7V12a2LqUHruhw6LQ5xggjdGMRIjAim4bdPx%2BUT75VYJdTcvhXjnvPOjLstxlMk5ZSL8IvpV2V6u%2FfOTNvbLar7mjqK5apewvryEq%2FnJTx76dvuruwlnJd4Cc%2F7QF6i19IqnzJteq2NERfwcOwQZ5%2FvY7Tiy2exlT%2BOs7B3WowqonJ9frmLN6P93e2F0%2F7zGsB7XbMKxF%2FA9Yv4tyD%2Bf7qN4aQXOAeb%2FtC7kT97F%2Ft8futv2l6L%2BBbHubUovvq2UxVGf3QxC%2Fv6YAnC3bM5FvyCHyOWlV6haksQC3%2FlRqVZcSioyG7qwa0OgD0TDmf1xmHWYASHrQOr1T7%2Fkk9EgJ%2F3jbCICD9Jee9xfuuEWo%2BZgxIUmCJFHprLeMIxnGjtV25ha8mdOMsHGMVKTa%2F6kdbyQNtLtqO3NFBRitZAQDHKamlmb65lNiCsjv6K9OoA1d39Cw%3D%3D)
구현한 API의 동작을 촬영한 데모 영상 링크

구현 방법 및 이유에 대한 간략한 설명
이메일과 비밀번호로 회원가입할 수 있는 엔드포인트를 구현해 주세요.

```
USERNAME_FIELD = "email"
REQUIRED_FIELDS = ["username"]
```

이메일로 로그인 할 수 있게 설정 변경

이메일과 비밀번호에 대한 유효성 검사를 구현해 주세요.
이메일 조건: @ 포함
=> AbstractUser을 그대로 사용하면 email필드가 다른 규칙이 섞여 있어서 재정의 후

```python
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        email = kwargs.get("email")
        if email and email.find("@") == -1:
            raise ParseError

        super().__init__(*args, **kwargs)
```

유저 생성시 @만 포함 되면 통과되도록 만들었습니다.
비밀번호 조건: 8자 이상 and 비밀번호는 반드시 암호화하여 저장해 주세요.

```python
if len(password) < 8:
    raise ParseError
```

이 부분도 다른 조건은 붙지 않도록 8자 이상이 되어야만 통과가 되도록 만들었습니다.
그후

```python
user.set_password(password)
```

set_password메서드를 통해 해쉬 및 비밀번호를 지정해 주었습니다.

JWT를 이용하기 위해 simplejwt 라이브러리를 사용했습니다.
회원가입시 로그인시 자동 토큰 발행되도록 만들었습니다.

페이지네이션 사용 게시글 조회
퀴리매개변수(?page=2)로 page정보를 받도록 만들었습니다.
없으면 자동으로 1로 설정이 됩니다.

특정 게시글 수정, 삭제
수정, 삭제는 작성자 조회를 위해 반드시 로그인을 해야 들어갈 수 있도록 설계
로그인 유저 != 작성자 이면 오류 발생

```python
raise PermissionDenied
```

그리고 관리를 더 편하게 하기 위해
functions폴더를 만들어 모델 기준으로 기능을 묶어서 관리하고 있습니다.
[functions폴더](https://github.com/sungin95/wanted-pre-onboarding-backend/tree/main/functions)

MySQL 연결

```
# .env 파일을 만들어서 내용을 연결하시면 됩니다.
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST="127.0.0.1"
DB_PORT=3306
```

API 명세(request/response 포함)

7

| URL       | URI                  | METHOD | 설명                             | request.body                       | response.body                                                                                                                                                                                                                                                                                                     | 완료 |
| --------- | -------------------- | ------ | -------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| /articles | /?page=2             | GET    | 페이지 네이션을 이용 게시판 조회 |                                    | [{'pk': 1, 'title': 'test title', 'context': 'test context'}, {'pk': 2, 'title': 'test title', 'context': 'test context'}, {'pk': 3, 'title': 'test title', 'context': 'test context'}, {'pk': 4, 'title': 'test title', 'context': 'test context'}, {'pk': 5, 'title': 'test title', 'context': 'test context'}] |      |
|           | /                    | POST   | 게시판 생성                      | {"title":xxx,"context":xxx}        | {"pk": 1, title":xxx,"context":xxx}                                                                                                                                                                                                                                                                               |      |
|           | /detail/<article_pk> | GET    | 조회한 게시판 정보 조회          |                                    | {'pk': 1, 'title': 'test title', 'context': 'test context'}                                                                                                                                                                                                                                                       |      |
|           | /detail/<article_pk> | PUT    | 조회한 게시판 정보 수정          | {"title":xxx,"context":xxx}        | {'pk': 1, "title":xxx, 'context': xxx}                                                                                                                                                                                                                                                                            |      |
|           | /detail/<article_pk> | DELETE | 조회한 게시판 정보 삭제          |                                    |                                                                                                                                                                                                                                                                                                                   |      |
| /accounts | /create              | POST   | 유저 생성                        | {"email": xxx@nab,"password": xxx} | {"pk":1, "email": xxx@nab,"password": xxx}                                                                                                                                                                                                                                                                        |      |
|           | /log-in              | POST   | 유저 로그인                      | {"email": xxx@nab,"password": xxx} | {"pk":1, "email": xxx@nab,"password": xxx}                                                                                                                                                                                                                                                                        |      |

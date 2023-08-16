# wanted-pre-onboarding-backend

백엔드 프리온보팅 인턴십 8월 사전 과제

성명: 이성인

애플리케이션의 실행 방법 (엔드포인트 호출 방법 포함)
배포 버전: xxx
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

구현한 API의 동작을 촬영한 데모 영상 링크

구현 방법 및 이유에 대한 간략한 설명

API 명세(request/response 포함)

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
[ERD](https://viewer.diagrams.net/?tags=%7B%7D&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=ERD.svg#R7VhrU6MwFP01nXE%2FuMNDav1YWqvrY9f342OEFLKGhE1SW%2Frr9wZCgeJq6%2Bg6Os50Bu7JTULuOYHTdNxBMtsTKI2PeYhpx7HCWccddhzHtnc8uGgkK5Cu6xRAJEhokirgnMyxAS2DTkiIZSNRcU4VSZtgwBnDgWpgSAg%2BbaaNOW3OmqIIt4DzANE2ek1CFRdoz9mu8H1Moric2e7uFC0JKpPNSmSMQj6tQe5uxx0IzlVxl8wGmOrilXW5%2FpFd06P77t7BqfyDLv3Di59Xm8Vgo3W6LJYgMFMvHnp%2BPx7tX239vklPRqdTa69%2Fd7BpulgPiE5MvS4lFma9KiuLKKckoYhB5I85U%2BemBUrgI0oiBvcBPBv0dP0HLBSB%2BvdNg%2BIpoEFMaHiEMj7RK5AKBfdl5MdckDkMiyg02QBAs1BGSk63kXGuewJsASqwhJyTsiz2AjpCUpmcgFOKUknu8gfWKQkSEWE%2BV4on5UB8wkIcmmjBcx4owe8XytH9VyTDkKargWc1KRpy9jBPsBIZpJjWhc7MRrPLeFrJ1u4aLG5I1oDIbJVoMfZiujPYWohFUIRqPndpvq0V5wNGGtMhCsQzpLCvyyjrIoSb2lIrKJfmGjK1WzKdSD1ngltShWqrmiwpHqt%2FilKmKCAsOspzhlsVcmZWqyEOfcc0F0RMwhCzXDAKKVRoSqsk5YSpvByeDz8o2sD67nU8eKABxHYVw0%2BnCzXgDLSFSC4iDIKdYi3aR%2BT15MZ9Xl5Zk7V12a2LqUHruhw6LQ5xggjdGMRIjAim4bdPx%2BUT75VYJdTcvhXjnvPOjLstxlMk5ZSL8IvpV2V6u%2FfOTNvbLar7mjqK5apewvryEq%2FnJTx76dvuruwlnJd4Cc%2F7QF6i19IqnzJteq2NERfwcOwQZ5%2FvY7Tiy2exlT%2BOs7B3WowqonJ9frmLN6P93e2F0%2F7zGsB7XbMKxF%2FA9Yv4tyD%2Bf7qN4aQXOAeb%2FtC7kT97F%2Ft8futv2l6L%2BBbHubUovvq2UxVGf3QxC%2Fv6YAnC3bM5FvyCHyOWlV6haksQC3%2FlRqVZcSioyG7qwa0OgD0TDmf1xmHWYASHrQOr1T7%2Fkk9EgJ%2F3jbCICD9Jee9xfuuEWo%2BZgxIUmCJFHprLeMIxnGjtV25ha8mdOMsHGMVKTa%2F6kdbyQNtLtqO3NFBRitZAQDHKamlmb65lNiCsjv6K9OoA1d39Cw%3D%3D)
구현한 API의 동작을 촬영한 데모 영상 링크

구현 방법 및 이유에 대한 간략한 설명

API 명세(request/response 포함)

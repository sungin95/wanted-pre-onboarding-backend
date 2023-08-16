from articles.models import Articles
from accounts.models import User
from rest_framework.exceptions import NotFound


def page_nation(page_size, page):
    try:
        page = int(page)
    except ValueError:
        page = 1
    page_size = page_size
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


def article_get_object(pk: int):
    try:
        return Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        raise NotFound


def article_create_test_list(n: int, user: User) -> list:
    articles_list = []
    for _ in range(n):
        article = Articles.objects.create(
            title="test title",
            context="test context",
            owner=user,
        )
        articles_list.append(article)
    return articles_list

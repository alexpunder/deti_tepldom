from django.db.models import Q, QuerySet

from .models import Blog


def get_filtered_blogs(
    category: str | None, search: str | None, tag: str | None,
) -> QuerySet[Blog]:
    """
    Получение отфильтрованых новостей по переданным параметрам:
    - category: категория новостей
    - tag: тег новостей
    - search: ключевое слово или фраза для поиска.
    """
    if category:
        blogs = Blog.objects.filter(
            category__slug=category
        ).select_related(
            'category'
        )
    elif search:
        blogs = Blog.objects.filter(
            Q(title__icontains=search)
            | Q(text__icontains=search)
            | Q(category__name__icontains=search)
            | Q(tag__name__icontains=search)
        ).select_related(
            'category'
        )
    elif tag:
        blogs = Blog.objects.filter(
            tags__slug=tag
        ).prefetch_related(
            'tags'
        )
    else:
        blogs = Blog.objects.all()

    return blogs

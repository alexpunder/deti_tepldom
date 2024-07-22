from django.contrib import messages
from django.db.models import QuerySet

from blog.models import Blog
from schooling.models import Project
from .filters import SearchBlogFilter, SearchProjectFilter


def search_filter(
    request, query: str | None
) -> tuple[int, QuerySet[Blog] | None, QuerySet[Project] | None] | None:
    """Получние новостей и проектов на основе запроса."""
    if not query or query.strip() == '':
        messages.warning(
            request,
            message=(
                'Пожалуйста, введите корректный запрос для поиска.'
            )
        )
        return None

    search_blogs = SearchBlogFilter(
        request.GET, queryset=Blog.objects.all()
    )
    search_projects = SearchProjectFilter(
        request.GET, queryset=Project.objects.all()
    )
    total_results = search_blogs.qs.count() + search_projects.qs.count()

    if not total_results:
        messages.warning(
            request,
            message=(
                'К сожалению, ничего найти не удалось... '
                'Попробуйте изменить свой запрос.'
            )
        )
        return None

    messages.success(
        request,
        message=f'Найдено совпадений: {total_results}'
    )
    return total_results, search_blogs.qs, search_projects.qs

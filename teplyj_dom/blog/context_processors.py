from teplyj_dom.constants import LATEST_NEWS_LIMIT

from .models import Blog


def latest_news(request):
    """Получение последних новостей для бокового меню в заголовке страницы."""
    latest_news = Blog.objects.order_by('-pub_date')[:LATEST_NEWS_LIMIT]
    return {'latest_news': latest_news}

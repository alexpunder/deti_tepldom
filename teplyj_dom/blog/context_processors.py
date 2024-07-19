from .models import Blog


def latest_news(request):
    latest_news = Blog.objects.order_by('-pub_date')[:3]
    return {'latest_news': latest_news}

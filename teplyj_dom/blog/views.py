from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from teplyj_dom.constants import BLOG_LIST_PAGINATION

from .models import Blog, Category
from .services import get_filtered_blogs


def blog_list(request):
    """
    Страница со списком всех новостей.

    Фильтрация по категории, тегу или параметру поиска: получение GET-запроса
    и дальнейшая передача в функцию get_filtered_blogs.
    """
    categories = Category.objects.all()
    category_slug = request.GET.get('category_slug')
    search = request.GET.get('news_search')
    tag = request.GET.get('tag')

    blogs = get_filtered_blogs(
        category=category_slug,
        search=search,
        tag=tag,
    )

    paginator = Paginator(blogs, BLOG_LIST_PAGINATION)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog_pages/blog_list.html',
        context={
            'page_obj': page_obj,
            'categories': categories,
        }
    )


def blog_details(request, blog_slug):
    """Детальная страница новости."""
    blog = get_object_or_404(Blog, slug=blog_slug)
    tags = blog.tags.all()
    return render(
        request,
        'blog_pages/blog_details.html',
        context={
            'blog': blog,
            'tags': tags,
        }
    )

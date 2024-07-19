from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Blog, Category


def blog_list(request):
    categories = Category.objects.all()
    category_slug = request.GET.get('category_slug')
    news_search = request.GET.get('news_search')
    tag = request.GET.get('tag')

    if category_slug:
        blogs = Blog.objects.filter(
            category__slug=category_slug
        ).select_related(
            'category'
        ).order_by(
            'pub_date'
        )

    elif news_search:
        blogs = Blog.objects.filter(
            Q(title__icontains=news_search)
            | Q(text__icontains=news_search)
            | Q(category__name__icontains=news_search)
        ).select_related(
            'category'
        ).order_by(
            'pub_date'
        )

    elif tag:
        blogs = Blog.objects.filter(
            tags__slug=tag
        ).prefetch_related(
            'tags'
        ).order_by(
            'pub_date'
        )

    else:
        blogs = Blog.objects.order_by(
            '-pub_date'
        )

    paginator = Paginator(blogs, 5)
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

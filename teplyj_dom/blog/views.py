from django.shortcuts import render


def blog_list(request):
    return render(
        request,
        'blog_pages/blog_list.html'
    )


def blog_details(request):
    return render(
        request,
        'blog_pages/blog_details.html'
    )

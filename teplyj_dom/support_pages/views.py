from django.shortcuts import render


def charity(request):
    return render(
        request,
        'support_pages/charity.html'
    )


def faq(request):
    return render(
        request,
        'support_pages/faq.html'
    )


def about(request):
    return render(
        request,
        'support_pages/about.html'
    )


def usefull_links(request):
    return render(
        request,
        'support_pages/usefull_links.html'
    )


def contacts(request):
    return render(
        request,
        'support_pages/contacts.html'
    )

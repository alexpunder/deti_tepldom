from django.shortcuts import render

from .models import AboutItem, OurTeam


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
    table_items = AboutItem.objects.all()
    return render(
        request,
        'support_pages/about.html',
        context={
            'table_items': table_items
        }
    )


def usefull_links(request):
    usefull_links = range(10)
    return render(
        request,
        'support_pages/usefull_links.html',
        context={'usefull_links': usefull_links}
    )


def contacts(request):
    return render(
        request,
        'support_pages/contacts.html'
    )


def team(request):
    teammates = OurTeam.objects.all()
    return render(
        request,
        'support_pages/team.html',
        context={'teammates': teammates}
    )

from django.shortcuts import render

from schooling.forms import SendQuestionForm
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
    form = SendQuestionForm()
    if request.method == 'POST':
        form = SendQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'scholling_pages/success.html'
            )
    return render(
        request,
        'support_pages/contacts.html',
        context={
            'form': form
        }
    )


def team(request):
    teammates = OurTeam.objects.all()
    return render(
        request,
        'support_pages/team.html',
        context={'teammates': teammates}
    )

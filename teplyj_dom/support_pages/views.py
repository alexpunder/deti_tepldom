from django.shortcuts import render

from schooling.forms import SendQuestionForm
from .models import (
    AboutItem, OurTeam, Document, UsefullLink, MassMedia, Charity,
)


def charity(request):
    charity_data = Charity.objects.all()
    return render(
        request,
        'support_pages/charity.html',
        context={
            'charity_data': charity_data,
        }
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


def documents(request):
    documents = Document.objects.all()
    return render(
        request,
        'support_pages/documents.html',
        context={
            'documents': documents,
        }
    )


def usefull_links(request):
    usefull_links = UsefullLink.objects.all()
    return render(
        request,
        'support_pages/usefull_links.html',
        context={'usefull_links': usefull_links}
    )


def mass_media(request):
    mass_media = MassMedia.objects.all()
    return render(
        request,
        'support_pages/mass_media.html',
        context={
            'mass_media': mass_media,
        }
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


def page_not_found(request, exception):
    return render(
        request,
        'support_pages/404.html',
        status=404
    )

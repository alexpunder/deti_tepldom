from asgiref.sync import async_to_sync
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from schooling.forms import SendQuestionForm
from schooling.utils import send_telegram_message

from .services import search_filter
from .models import (AboutItem, Charity, Document, MassMedia, OurTeam,
                     Question, UsefullLink)


def search(request):
    """Обработчик поиска в заголовке страницы."""
    query = request.GET.get('search')

    result = search_filter(request=request, query=query)

    if not result:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    total_results, search_blogs, search_projects = result

    return render(
        request,
        'support_pages/search_results.html',
        context={
            'query': query,
            'total_results': total_results,
            'blogs': search_blogs,
            'projects': search_projects,
        }
    )


def contacts(request):
    """
    Страница контактов. Содержит форму для отправки вопросов администратору
    через телеграм-бота в группу.
    """
    form = SendQuestionForm()
    if request.method == 'POST':
        form = SendQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            async_to_sync(send_telegram_message)(**form.cleaned_data)
            messages.success(
                request,
                'Обращение отправлено!'
            )
            return render(
                request,
                'schooling_pages/success.html'
            )
        else:
            model = form._meta.model
            for field, errors in form.errors.items():
                field_verbose_name = model._meta.get_field(field).verbose_name
                for error in errors:
                    messages.error(request, f'{field_verbose_name}: {error}')

    return render(
        request,
        'support_pages/contacts.html',
        context={
            'form': form
        }
    )


def charity(request):
    """Страница реквизитов организации для пожертвований."""
    charity_data = Charity.objects.all()
    return render(
        request,
        'support_pages/charity.html',
        context={
            'charity_data': charity_data,
        }
    )


def faq(request):
    """Страница с ответами на вопросы."""
    questions = Question.objects.all()
    return render(
        request,
        'support_pages/faq.html',
        context={
            'questions': questions,
        }
    )


def about(request):
    """Страница с описанием и информацией о деятельности организации."""
    table_items = AboutItem.objects.all()
    return render(
        request,
        'support_pages/about.html',
        context={
            'table_items': table_items
        }
    )


def documents(request):
    """Страница с правовыми и прочими документами организации."""
    documents = Document.objects.all()
    return render(
        request,
        'support_pages/documents.html',
        context={
            'documents': documents,
        }
    )


def usefull_links(request):
    """Страница с ссылками на административные ресурсы."""
    usefull_links = UsefullLink.objects.all()
    return render(
        request,
        'support_pages/usefull_links.html',
        context={'usefull_links': usefull_links}
    )


def mass_media(request):
    """Страница с ссылками на статьи в СМИ."""
    mass_media = MassMedia.objects.all()
    return render(
        request,
        'support_pages/mass_media.html',
        context={
            'mass_media': mass_media,
        }
    )


def team(request):
    """Страница с персоналом организации."""
    teammates = OurTeam.objects.all()
    return render(
        request,
        'support_pages/team.html',
        context={'teammates': teammates}
    )


def page_not_found(request, exception):
    """Обработчик страницы ошибки 404."""
    return render(
        request,
        'support_pages/404.html',
        status=404
    )

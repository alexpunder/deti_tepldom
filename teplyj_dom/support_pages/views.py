from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from blog.models import Blog
from schooling.models import Project
from schooling.forms import SendQuestionForm
from schooling.utils import send_telegram_message
from .models import (
    AboutItem, OurTeam, Document, UsefullLink, MassMedia, Charity, Question
)
from .filters import SearchBlogFilter, SearchProjectFilter


def search(request):
    query = request.GET.get('search')

    if not query or query.strip() == '':
        messages.warning(
            request,
            message=(
                'Пожалуйста, введите корректный запрос для поиска.'
            )
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    search_blogs = SearchBlogFilter(
        request.GET, queryset=Blog.objects.all()
    )
    search_projects = SearchProjectFilter(
        request.GET, queryset=Project.objects.all()
    )
    total_results = search_blogs.qs.count() + search_projects.qs.count()

    if not total_results:
        messages.warning(
            request,
            message=(
                'К сожалению, ничего найти не удалось... '
                'Попробуйте изменить свой запрос.'
            )
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    messages.success(
        request,
        message=f'Найдено совпадений: {total_results}'
    )

    return render(
        request,
        'support_pages/search_results.html',
        context={
            'query': query,
            'total_results': total_results,
            'blogs': search_blogs.qs,
            'projects': search_projects.qs,
        }
    )


def contacts(request):
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
    charity_data = Charity.objects.all()
    return render(
        request,
        'support_pages/charity.html',
        context={
            'charity_data': charity_data,
        }
    )


def faq(request):
    questions = Question.objects.order_by('id')
    return render(
        request,
        'support_pages/faq.html',
        context={
            'questions': questions,
        }
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

from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.views.generic import ListView

from .models import Project, MainGallery
from .forms import SendQuestionForm
from .utils import send_telegram_message


def index(request):
    images = MainGallery.objects.all()
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
        'index.html',
        context={
            'form': form,
            'images': images,
        }
    )


class ProjectsListView(ListView):
    queryset = Project.objects.all()
    template_name = 'schooling_pages/projects_list.html'
    paginate_by = 1


def projects(request):
    project_items = Project.objects.all()
    return render(
        request,
        'schooling_pages/projects_list.html',
        context={
            'project_items': project_items,
        }
    )


def project_details(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    project_images = project.images.all()
    return render(
        request,
        'schooling_pages/project_details.html',
        context={
            'project': project,
            'project_images': project_images,
        }
    )

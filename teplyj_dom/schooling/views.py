from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Project, MainGallery
from .forms import SendQuestionForm


def index(request):
    images = MainGallery.objects.all()
    form = SendQuestionForm()
    if request.method == 'POST':
        form = SendQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                'schooling_pages/success.html'
            )
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

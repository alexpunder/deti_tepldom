from django.shortcuts import get_object_or_404, render

from .models import Project
from .forms import SendQuestionForm


def index(request):
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
            'form': form
        }
    )


def projects(request):
    project_items = Project.objects.all()
    return render(
        request,
        'schooling_pages/projects_list.html',
        context={
            'project_items': project_items,
        }
    )


def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(
        request,
        'schooling_pages/project_details.html',
        context={
            'project': project,
        }
    )

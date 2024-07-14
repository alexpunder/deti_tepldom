from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html',
    )


def projects(request):
    return render(
        request,
        'scholling_pages/projects_list.html'
    )


def project_details(request, prject_id):
    pass

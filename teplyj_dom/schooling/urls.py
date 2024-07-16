from django.urls import path

from .views import index, project_details, ProjectsListView

app_name = 'schooling'

urlpatterns = [
    path('', index, name='index'),
    path(
        'projects',
        ProjectsListView.as_view(),
        name='projects'
    ),
    path(
        'projects/<slug:project_slug>',
        project_details,
        name='project_details'
    ),
]

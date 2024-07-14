from django.urls import path

from .views import index, projects, project_details

app_name = 'schooling'

urlpatterns = [
    path('', index, name='index'),
    path('projects', projects, name='projects'),
    path('projects/<int:project_id>', project_details, name='project_details'),
]

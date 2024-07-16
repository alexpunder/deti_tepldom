from django.urls import path

from .views import blog_list, blog_details

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<slug:blog_slug>', blog_details, name='blog_details'),
]

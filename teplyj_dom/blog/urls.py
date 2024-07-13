from django.urls import path

from .views import blog_list, blog_details

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('/1', blog_details, name='blog_details'),
]

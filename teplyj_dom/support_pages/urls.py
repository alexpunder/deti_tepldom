from django.urls import path

from .views import charity, faq, about, usefull_links, contacts

app_name = 'support'

urlpatterns = [
    path('about', about, name='about'),
    path('charity', charity, name='charity'),
    path('contacts', contacts, name='contacts'),
    path('faq', faq, name='faq'),
    path('usefull_links', usefull_links, name='usefull_links'),
]

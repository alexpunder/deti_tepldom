from django.urls import path

from .views import (
    charity, faq, about, usefull_links, contacts, team, documents,
    mass_media, search,
)

app_name = 'support'

urlpatterns = [
    path('about', about, name='about'),
    path('charity', charity, name='charity'),
    path('contacts', contacts, name='contacts'),
    path('documents', documents, name='documents'),
    path('faq', faq, name='faq'),
    path('mass-media', mass_media, name='mass_media'),
    path('search', search, name='search'),
    path('team', team, name='team'),
    path('usefull-links', usefull_links, name='usefull_links'),
]

from employee.models import About
from django import urls
from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contact, name='contact')
]

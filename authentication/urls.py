from os import name
from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.authlogin, name='login'),
    path('register/', views.authregister, name='register'),
    path('private/', views.logedrouter, name='private')
]

from django.http import HttpResponse
from django.shortcuts import render


def employee(request):
    
    return render(request, 'employee/index.html')


def profile(request):
    teste = {
        'name': 'james'
    }
    return render(request, 'employee/profile.html', teste)

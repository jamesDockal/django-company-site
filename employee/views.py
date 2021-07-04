from django.http import HttpResponse
from django.shortcuts import render

from .models import About


def aboutus(request):

    aboutdata = {
        'data': About.objects.all()
    }

    # print(f' about data ${aboutdata}')

    return render(request, 'employee/about.html', aboutdata)


def projects(request):
    teste = {
        'name': 'james'
    }
    return render(request, 'employee/projects.html', teste)

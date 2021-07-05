from django.http import HttpResponse
from django.shortcuts import render

from .models import About, Contact


def aboutus(request):
    aboutdata = {
        'data': About.objects.all()
    }

    return render(request, 'employee/about.html', aboutdata)


def projects(request):
    teste = {
        'name': 'james'
    }
    return render(request, 'employee/projects.html', teste)


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        text = request.POST.get('text')

        Contact(email=email, text=text).save()

    return render(request, 'employee/contact.html')

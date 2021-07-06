from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def logedrouter(request):

    return HttpResponse('aaaaaaaaaaaaaaa')


def authlogin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('private')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'auth/login.html')


def authregister(request):

    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username == '':
            messages.error(request, 'No name provided')

        elif email == '':
            messages.error(request, 'No email provided')

        elif password == '':
            messages.error(request, 'No password provided')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username alredy in use')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email alredy in use')

        elif User.objects.filter(password=password).exists():
            messages.error(request, 'Password alredy in use')

        else:
            User.objects.create_user(
                username=username, email=email, password=password).save()
            messages.success(request, 'User Created!')
            # login(request, user)

            return redirect('login')

    return render(request, 'auth/register.html')

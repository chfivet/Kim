from django.shortcuts import render


def home(request):
    return render(request, 'common/home.html')


def login(request):
    return render(request, 'common/login.html')

from django.contrib.auth import authenticate
from django.shortcuts import redirect


def validation_user(request):
    return redirect('/common/')

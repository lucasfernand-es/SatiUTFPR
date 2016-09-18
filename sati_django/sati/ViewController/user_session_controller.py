from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse

from sati.models import Person


def user_authenticate(username, password):
    print password, username
    user = authenticate(username=username, password=password)
    return user;


def user_session(request):
    if request.session.get('has_logged', False):
        return True
    else:
        return False


def user_login(request):
    user = user_authenticate(request.POST.get('username'), request.POST.get('userpass'))
    if user is not None:
        login(request, user)
        return render(
            request,
            'dashboard/index.html',
        )
    else:
        return render(
            request,
            'public/login.html'
        )


def user_logout(request):
    logout(request)
    return render(request,
                  'public/index.html')


def user_signup(request):
    person = Person()
    print request

    return JsonResponse(2)
    # return render(
    #    request,
    #    'sati_utfpr/test.html'
    #)

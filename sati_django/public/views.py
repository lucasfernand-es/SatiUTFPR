from django.shortcuts import render, render_to_response
from sati_system import session
# from django.http import HttpResponse


# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'public/index.html')


def login(request):
    if request.session.get('has_logged'):
        return render(request, 'dashboard/index.html')
    else:
        return render(request, 'public/login.html')


def signup(request):
    return render(request, 'public/signup.html')


def new_login(request):
    return render(request, 'public/login.html')
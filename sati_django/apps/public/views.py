from django.shortcuts import render, render_to_response
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    print "index"
    return render(request, 'public/index.html')


def login(request):
    print "login"
    print request.user.is_authenticated
    print request.user.username
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html')
    else:
        return render(request, 'public/login.html')


def signup(request):
    return render(request, 'public/signup.html')


def new_login(request):
    return render(request, 'public/login.html')

# Events


def event(request):
    return render(request, 'event/index.html')


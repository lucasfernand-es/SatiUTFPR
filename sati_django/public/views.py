from django.shortcuts import render, render_to_response
# from django.http import HttpResponse


# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'public/index.html')


def login(request):
    return render(request, 'public/login.html')


def signup(request):
    return render(request, 'public/signup.html')

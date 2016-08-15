from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from controller import LoginController

# Create your views here.

# class LunchForm(forms.Form):
#     submitter = forms.CharField(label='Your name')
#     food = forms.CharField(label='What did you eat?')
#
#
# lunch_form = LunchForm(auto_id=False)


def index(request):
    # lunches = Lunch.objects.all()
    return render(
        request,
        'sati_utfpr/index.html'
    )


def login(request):
    return render(
        request,
        'sati_utfpr/login.html'
    )

def test(request):
    return render(
        request,
        'sati_utfpr/test.html'
    )

def newLogin(request):
    loginController = LoginController(request)
    return loginController.newLogin()

# import os, sys
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ViewController import LoginController
from VO.VOHelper import Acess
from VO.VOHelper import Status


def index(request):
    # lunches = Lunch.objects.all()
    return render(
        request,
        'sati_utfpr/index.html'
    )


def test(request):
    return render(
        request,
        'sati_utfpr/test.html'
    )


def login(request):
    return render(
        request,
        'public/login.html'
    )


def newLogin(request):
    loginController = LoginController(request)
    return loginController.newLogin()



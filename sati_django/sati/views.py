# import os, sys
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from controller import LoginController
from VO.VOHelper import Acess
from VO.VOHelper import Status

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


def signup(request):
    return render(
        request,
        'sati_utfpr/signup.html'
    )


def newLogin(request):
    loginController = LoginController(request)
    return loginController.newLogin()



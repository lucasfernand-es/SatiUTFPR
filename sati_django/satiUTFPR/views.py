# import os, sys
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from controller import LoginController
from models import Person
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


def registry_person(request):
    person = Person()
    person.name = request.POST["nome_completo"]
    person.dateBirth = request.POST["data_nascimento"]
    person.institution = request.POST["instituicao"]
    person.password = request.POST["senha"]
    person.cpf = request.POST["cpf"]
    person.academicRegistry = request.POST["registro_academico"]
    person.role = 0
    person.status = 1
    person.save()
    return render(
        request,
        'sati_utfpr/test.html'
    )
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
import json

from sati.models import Person
from sati_django.sati.serializers import *


def user_authenticate(username, password):
    print password, username
    user = authenticate(username=username, password=password)
    return user


def user_session(request):
    if request.session.get('has_logged', False):
        return True
    else:
        return False


def user_login(request):
    # required_login = json.loads(request.body)

    user = user_authenticate('email@email.com', '123')  # (required_login['email'], required_login['password'])

    if user is not None:
        login(request, user)

        print 'oi passou'

        return HttpResponse(
            'dashboard/index.html'
        )
    else:
        return HttpResponse(
            'public/login.html'
        )


def user_logout(request):
    logout(request)
    return render(request,
                  'public/index.html')


def user_signup(request):

    if request.method == 'POST':
        print 'postou algo'
        print request.body

        person = json.loads(request.body)
        print person['name']

        serializer = PersonSerializer(data=person)
        if serializer.is_valid():
            # serializer.save()
            print 'save'
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print 'nope'

        serializer.errors.sessions = 'Vários erros'

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    print 'chegou aqui'
    return JsonResponse(2, safe=False)
    # return render(
    #    request,
    #    'sati_utfpr/test.html'
    # )
#    if request.POST["nome_completo"]:
#        person.name = request.POST["nome_completo"]
#
#    person.institution = request.POST["instituicao"]
#    if request.POST["senha"] == request.POST.get('confirmar_senha', '') and request.POST["senha"]:
#        person.password = request.POST["senha"]
#    else:
#        NotImplementedError
#
#    if request.POST["cpf"]:
#        person.cpf = request.POST["cpf"]
#    else:
#        NotImplementedError
#
#    if request.POST["email"]:
#        person.email = request.POST["email"]
#    else:
#        NotImplementedError
#
#    if person.institution and person.institution == "UTFPR":
#        person.academicRegistry = request.POST["registro_academico"]
#    else:
#        NotImplementedError
#
#    # Valores padrao 0 aluno e 1 para ativo
#    person.role = 0
#    person.status = 1
#
#    # usuario para autenticacao e login
#    verify_person_cpf = False #Person.objects.get(cpf=person.cpf)
#    verify_person_email = False #Person.objects.get(email=person.email)
#
#    if not verify_person_cpf and not verify_person_email:
#        user = User()
#        user.password = person.password
#        user.username = person.email
#        user.save()
#
#        person.user = user
#        person.save()
#    else:
#        NotImplementedError
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.db import Error
import json

from sati.models import Person, Participant, Session
from sati.serializers import *


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
    user = {"email": request.POST.get('email'), 'password': request.POST.get('password')}
    # required_login = json.loads(request.body)
    print user
    print 'user'

    user = user_authenticate(user['email'], user['password'])  # (required_login['email'], required_login['password'])

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(
            request,
            '/dashboard/'
        )
    else:
        oops = 'Ops! Ocorreu um erro inesperado. Tente novamente.'
        return HttpResponseRedirect(
            '/login/'
        )


def user_logout(request):
    logout(request)
    return render(request,
                  'public/index.html')

@csrf_exempt
def user_signup(request):

    if request.method == 'POST':
        print 'postou algo'
        print request.body

        print
        person = json.loads(request.body)
        person['is_active'] = True
        person['role'] = 0

        if 'password' in person:
            if ('confirm_password' not in person) or person['password'] != person['confirm_password']:
                error = {'confirm_password': 'As senhas informadas devem ser iguas.'}
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(data=person)

        if serializer.is_valid():
            print "SIM É VALIDO"
            try:
                person_response = serializer.save()
            except:
                person_response = None

            if person_response is not None:
                errors_array = []
                for id_session in person['sessions']:
                    participant = Participant()
                    participant.person = person_response
                    participant.session = Session.objects.get(id=id_session)
                    participant.is_confirmed = False
                    participant.status = False
                    try:
                        participant.save()
                    except Error:
                        errors_array.append('error_session_' + str(id_session))
                if len(errors_array):
                    return JsonResponse({'errors': errors_array}, status=status.HTTP_400_BAD_REQUEST)
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer.errors.sessions = 'Vários erros'
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # print 'chegou aqui'
    # return JsonResponse(2, safe=False)
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
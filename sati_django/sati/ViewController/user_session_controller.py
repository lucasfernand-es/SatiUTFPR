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
    try:
        user = authenticate(username=username, password=password)
    except User.DoesNotExist:
        return None
    return user


def user_session(request):
    if request.session.get('has_logged', False):
        return True
    else:
        return False


def user_login(request):
    user = {"email": request.POST.get('email'), 'password': request.POST.get('password')}
    # required_login = json.loads(request.body)

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


def get_user_participant(request):
    # print 'olaaar algo'
    # print request.body

    sent_user = json.loads(request.body)
    # person['is_active'] = True

    user = {"email": sent_user['email'], 'password': sent_user['password']}
    # required_login = json.loads(request.body)

    user = user_authenticate(user['email'], user['password'])  # (required_login['email'], required_login['password'])

    if user is not None:
        # THERE IS NO WAY .GET WILL RETURN NONE
        person = Person.objects.get(email=sent_user['email'])
        participates = Participant.objects.filter(person_id=person.id, status=True)
        session_array = []
        for participate in participates:
            session_array.append({
                'id': participate.session.id,
            })

        serializer = PersonSerializer(person, many=False)
        person = serializer.data
        # print person

        return JsonResponse({
            'error': False,
            'sessions': session_array,
            'person': person
        })
    else:
        oops = 'Usuário não cadastrado ou senha/email inválidos.'
        # print oops
        return JsonResponse({
            'error': True,
            'error_messages': oops,
        })


def user_update_participant(request):
    # print request.body

    update_participant = json.loads(request.body)

    sessions = update_participant['sessions']
    person_id = update_participant['id']
    person = Person.objects.get(id=person_id)
    errors_array = []
    sessions_array = []
    for session in sessions:
        participants = Participant.objects.filter(session_id=session, person_id=person_id)
        if not len(participants):
            participant = Participant()
            participant.person = person
            participant.session = Session.objects.get(id=session)
            participant.is_confirmed = False
            participant.status = True
            try:
                participant.save()
                sessions_array.append({'event_name': participant.session.event.name, 'new': True})
            except Error:
                errors_array.append('error_session_' + str(session.id))

        else:
            for participant in participants:
                sessions_array.append({'event_name': participant.session.event.name, 'new': False})
        #
        #        participant.status = not participant.status
        #        try:
        #            participant.save()
        #       except Error:
        #            errors_array.append('error_session_' + str(session.id))

    if len(errors_array):
        return JsonResponse({
            'error': True,
            'error_messages': errors_array
        })
    else:
        serializer = PersonSerializer(person, many=False)
        data = serializer.data
        return JsonResponse({
            'person': data,
            'sessions': sessions_array,
            'error': False,
            'status': status.HTTP_201_CREATED
        })

@csrf_exempt
def user_signup(request):

    if request.method == 'POST':
        # print 'postou algo'
        # print request.body

        person = json.loads(request.body)
        person['is_active'] = True
        person['role'] = 0

        if 'password' in person:
            if ('confirm_password' not in person) or person['password'] != person['confirm_password']:
                error = {'confirm_password': 'As senhas informadas devem ser iguas.'}
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)

        if 'academic_registry' in person:
            if not person['academic_registry']:
                del person['academic_registry']

        # print person
        serializer = PersonSerializer(data=person)

        if serializer.is_valid():
            try:
                person_response = serializer.save()
            except:
                person_response = None

            if person_response is not None:
                errors_array = []
                sessions_array = []
                for id_session in person['sessions']:
                    participant = Participant()
                    participant.person = person_response
                    participant.session = Session.objects.get(id=id_session)
                    participant.is_confirmed = False
                    participant.status = True
                    try:
                        participant.save()
                        sessions_array.append({'event_name': participant.session.event.name})
                    except Error:
                        errors_array.append('error_session_event_' + participant.session.event.name)
                if len(errors_array):
                    return JsonResponse({'errors': errors_array}, status=status.HTTP_400_BAD_REQUEST)
                return JsonResponse({'person': serializer.data, 'sessions': sessions_array}, status=status.HTTP_201_CREATED)
        else:
            serializer.errors.sessions = 'Vários erros'
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

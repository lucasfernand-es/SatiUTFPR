# -*- coding: utf-8 -*-
from sati.models import Person, Session, Participant, Event
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from rest_framework import status
from sati.serializers import *
from django.db import Error
import json


@login_required
def confirm_participant(request):
    if request.user.is_superuser:
        # print request.body

        body = json.loads(request.body)
        participants = body['participants']

        errors_array = []
        success_array = []
        has_error = False
        if participants is not None:
            for part in participants:
                participant_id = part['id']
                session_id = part['session_id']
                is_confirmed = part['is_confirmed']

                participant = Participant.objects.get(id=participant_id)

                if participant.is_confirmed == is_confirmed:
                    success_array.append({'participant': create_participant_json(participant), 'is_new': False})
                else:
                    if not is_confirmed:
                        participant.is_confirmed = False
                        try:
                            participant.save()
                            success_array.append({'participant': create_participant_json(participant), 'is_new': True})
                        except Error:
                            has_error = True
                            errors_array.append({'participant': create_participant_json(participant),
                                                 'error_type': 'Server Problem'})
                    else:
                        if get_session_available_spots(session_id) > 0:
                            participant.is_confirmed = True
                            try:
                                participant.save()
                                success_array.append({
                                    'participant': create_participant_json(participant),
                                    'is_new': True,
                                })
                            except Error:
                                has_error = True
                                errors_array.append({
                                    'participant': create_participant_json(participant),
                                    'error_type': 'Server Problem'
                                })
                        else:
                            has_error = True
                            errors_array.append({
                                'participant': create_participant_json(participant),
                                'error_type': 'Turma lotada'
                            })
            # if has_error:
            #    return JsonResponse({
            #        'error': True,
            #        'error_messages': errors_array,
            #        'success_message': success_array,
            #    })
            # else:
            return JsonResponse({
                'success_message': success_array,
                'error_messages': errors_array,
                'status': status.HTTP_100_CONTINUE
            })
        else:
            return JsonResponse({
                'error': True,
                'empty': True,
                'error_messages': 'ID da turma não encontrado'
            })


@login_required
def get_all_participants(request):
    if request.user.is_superuser:
        events = Event.objects.all()

        events_array = []
        for event in events:
            sessions = Session.objects.filter(event_id=event.id)
            sessions_array = []
            for session in sessions:
                participants = Participant.objects.filter(session_id=session.id, status=True)
                participants_array = []
                for participant in participants:
                    participants_array.append(create_participant_json(participant))

                sessions_array.append(create_session_json(session, participants_array))
            events_array.append(create_event_json(event, sessions_array))

        # print create_response('events', events_array, False, {})
        return JsonResponse(create_response('events', events_array, False, {}))
    else:
        return HttpResponseForbidden

def create_response(response_key, response, error, error_messages):
    return{
        response_key: response,
        'error': error,
        'error_messages': error_messages,
        'status_code' : status.HTTP_100_CONTINUE,

    }


def create_event_json(event, sessions_array):
    return {
        'name': event.name,
        'fee': event.fee,
        'id': event.id,
        'edition_name': event.edition.name,
        'category_name': event.category.name,
        'sessions': sessions_array,
    }


def create_session_json(session, participant_array):
    occurrences = Occurrence.objects.filter(session_id=session.id)
    occurrences_array = []
    for occurrence in occurrences:
        occurrences_array.append(create_occurrence_json(occurrence))
    return {
        'instructor_name': session.instructor.name,
        'spots': session.spots,
        'available_spots': get_session_available_spots(session.id),
        'has_spots': get_session_available_spots(session.id) > 0,
        'occurrences': occurrences_array,
        'participants': participant_array,
    }


def create_occurrence_json(occurrence):
    return {
        'begin_date_time': occurrence.begin_date_time,
        'end_date_time': occurrence.end_date_time,
        'room': occurrence.room.name

    }


def create_participant_json(participant):
    return {
        'id': participant.id,
        'is_confirmed': participant.is_confirmed,
        'name': participant.person.name,
        'person_id': participant.person.id,
        'session_id': participant.session.id,
        'event_name': participant.session.event.name,
        'cpf': participant.person.cpf,
        'academic_registry': participant.person.academic_registry
    }


def get_session_available_spots(session_id):
    participants = Participant.objects.filter(is_confirmed=True, session_id=session_id)
    session = Session.objects.get(id=session_id)

    if session:
        available_spots = session.spots - len(participants)
        if available_spots > 0:
            response = available_spots
        else:
            response = 0
    else:
            response = 0

    return response


def session_available_spots(session_id):
    participants = Participant.objects.filter(is_confirmed=True, session_id=session_id)
    session = Session.objects.get(id=session_id)

    response = 0

    if session:
        available_spots_session = session.spots - len(participants)
        if available_spots_session > 0:
            response = available_spots_session

    return response


def event_available_spots(event_id):
    sessions = Session.objects.filter(event_id=event_id)

    response = 0

    if sessions:
        available_spots_event = 0
        for session in sessions:
            available_spots_event += session_available_spots(session.id)

        if event_available_spots > 0:
            response = available_spots_event

    return response


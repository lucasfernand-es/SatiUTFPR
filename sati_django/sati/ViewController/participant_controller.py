from sati.models import Person, Session, Participant, Event
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from sati_django.sati.serializers import *


def get_all_participants(request):
    events = Event.objects.all()

    events_array = []
    for event in events:
        sessions = Session.objects.filter(event_id=event.id)
        sessions_array = []
        for session in sessions:
            participants = Participant.objects.filter(session_id=session.id)
            participants_array = []
            for participant in participants:
                participants_array.append(create_participant_json(participant))

            sessions_array.append(create_session_json(session, participants_array))
        events_array.append(create_event_json(event, sessions_array))

    return JsonResponse(create_response('events', events_array, False, {}))


def create_response(response_key, response, error, error_messages):
    return{
        response_key : response,
        'error': error,
        'error_messages': error_messages,
        'status_code' : status.HTTP_100_CONTINUE,

    }

def create_event_json(event, sessions_array):
    return {
        'event': EventSerializer(data=event),
        'sessions': sessions_array,
    }

def create_session_json(session, participant_array):
    return {
        'session': session,
        'participants': participant_array
    }


def create_participant_json(participant):
    return {
        'participant_id': participant.id,
        'participant_is_confirmed': participant.is_confirmed,
        'person_name': participant.person.name,
        'person_cpf': participant.person.cpf,
        'person_academic_registry': participant.person.academic_registry
    }
# def get_all_participants(request):
#     persons = Person.objects.all()
#
#     if persons:
#         persons_array = []
#         for person in persons:
#             participate = Participant.objects.filter(person_id=person.id)
#             if not len(participate):
#                 continue
#             sessions_array = []
#             for registry in participate:
#                 session = Session.objects.filter(id=registry.session.id)
#                 sessions_array.append(create_session_json(session))
#             participate_json ={
#                 'sessions': sessions_array
#             }
#
# def create_session_json(session):
#     return {
#         'event_id' : session.event_id
#     }
#
# def create_person_dict(person):
#     return {
#         'cpf': person.cpf,
#         'name': person.name,
#         'academic_registry': person.academic_registry
#     }
#
#
# def create_json_response(response_key, response_dict, error, error_messages):
#     return {
#         response_key : response_dict,
#         'error': error,
#         'error_messages': error_messages
#     }


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


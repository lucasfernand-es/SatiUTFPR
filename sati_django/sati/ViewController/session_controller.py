# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, HttpResponse
from django.http import JsonResponse
from sati.models import *
from sati.ViewController.participant_controller import *


def create_json_response(available_spots, error, error_message):
    return JsonResponse({'available_spots': available_spots,
                         'error': error,
                         'error_message': error_message})


def get_events_spots(request, event_id):
    sessions = Session.objects.filter(event_id=request.POST.get(event_id))
    context = {}

    if sessions:
        spots_event = 0
        for session in sessions:
            spots_event += session.spots
        context['event_spots'] = spots_event
        context['error'] = False
    else:
        context['error'] = True
        context['error_msg'] = 'session_not_found'
    return HttpResponse(context)


def get_events_spots_available(request, event_id):
    sessions = Session.objects.filter(event_id=event_id)

    if sessions:
        event_available_spots = 0
        for session in sessions:
            participants = Participant.objects.filter(is_confirmed=True, session_id=session.id)
            session_available_spots = session.spots - len(participants)
            event_available_spots += session_available_spots

        if event_available_spots > 0:
            response = create_json_response(event_available_spots, False, '')

        else:
            response = create_json_response(0, False, 'no_spots_available')
    else:
        response = create_json_response(0, True, 'session_not_found')

    return HttpResponse(response)


def get_session_spots(request, event_id, session_id):
    session = Session.objects.filter(id=request.POST.get(session_id))
    context = {}

    if session:
        context['error'] = False
        context['session_spots'] = session.spots
    else:
        context['error'] = True
        context['error_msg'] = 'session_not_found'

    return HttpResponse(context)


def get_session_available_spots(request, session_id):
    participants = Participant.objects.filter(is_confirmed=True, session_id=session_id)
    session = Session.objects.get(id=session_id)

    if session:
        session_available_spots = session.spots - len(participants)
        if session_available_spots > 0:
            response = create_json_response(session_available_spots, False, '')
        else:
            response = create_json_response(0, False, 'no_spots_available')
    else:
            response = create_json_response(0, True, 'session_not_found')

    return HttpResponse(response)


def get_all_sessions(request):
    events = Event.objects.filter(is_active=True)
    response = []
    session_array = []

    for event in events:
        sessions = Session.objects.filter(event_id=event.id, is_active=True)

        for session in sessions:
            occurrences = Occurrence.objects.filter(session_id=session.id, is_active=True)
            occurrences_array = []
            for occurrence in occurrences:
                occurrences_json = {
                    'room': occurrence.room.name,
                    'begin_date_time': occurrence.begin_date_time,
                    'end_date_time': occurrence.end_date_time,
                }
                occurrences_array.append(occurrences_json)

            available_spots = session_available_spots(session.id)
            session_json = {
                'id': session.id,
                'instructor_name': session.instructor.name,
                'spots': session.spots,
                'available_spots': available_spots,
                'has_spots': available_spots > 0,
                'occurrences': occurrences_array,
                'category_name': event.category.name,
                'event_name': event.name,
                'event_fee': event.fee,
            }
            session_array.append(session_json)

    response = {
        'error': False,
        'sessions': session_array
    }
    return JsonResponse(response)

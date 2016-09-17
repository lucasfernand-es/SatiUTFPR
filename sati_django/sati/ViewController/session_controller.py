from django.shortcuts import render, render_to_response, HttpResponse
from django.http import JsonResponse
from sati.models import Session, Participant, Event


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

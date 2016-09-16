from django.shortcuts import render, render_to_response
from sati.models import Session, Participant, Event


def get_events_spots(request):
    sessions = Session.objects.filter(event_id=request.POST.get('event_id'))
    context = {}

    if sessions:
        for session in sessions:
            spots_event = session.spots + spots_event
        context['event_spots'] = spots_event
        context['error'] = False
    else:
        context['error'] = True
        context['error_msg'] = 'session_not_found'
    return context


def get_session_spots(request):
    session = Session.objects.filter(id=request.POST.get('session_id'))
    context = {}

    if session:
        context['error'] = False
        context['session_spots'] = session.spots
    else:
        context['error'] = True
        context['error_msg'] = 'session_not_found'

    return context

def get_session_available_spots(request):
    participants = Participant.objects.filter(is_confirmed=True, session_id=request.POST.get('session_id'))
    session = Session.objects.filter(id=request.POST.get('session_id'))
    context = {}

    if session:
        session_available_spots = session.spots - len(participants)
        if session_available_spots > 0:
            context['session_available_spots'] = session_available_spots
            context['error'] = False
        else:
            context['error_msg'] = 'no_spots_available'
            context['error'] = True
    else:
        context['error'] = True
        context['error_msg'] = 'session_not_found'
        


    return context
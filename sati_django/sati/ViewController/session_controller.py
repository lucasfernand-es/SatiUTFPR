from django.shortcuts import render, render_to_response
from sati.models import Session, Participant


def get_session_spots(request):
    session = Session.objects.filter(id=request.POST.get('event_id'))
    context = {
        'session_spots' : session.spots
    }
    return context

def get_session_available_spots(request):
    participants = Participant.objects.filter(is_confirmed=True, event_id=request.POST.get('event_id'))
    session = Session.objects.filter(id=request.POST.get('event_id'))
    session_available_spots = session.spots - len(participants)
    if session_available_spots > 0:
        context ={
            'session_available_spots': session_available_spots
        }
    else:
        context = {
            'error' : 'not_spots_available'
        }

    return context
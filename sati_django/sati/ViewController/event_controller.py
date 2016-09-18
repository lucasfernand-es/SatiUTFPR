from sati.models import Event, Edition, Session, Occurrence, Category
from sati.serializers import *
from django.shortcuts import render, render_to_response
from django.http import HttpResponseForbidden
from django.http import JsonResponse, HttpResponse
from sati.ViewController.participant_controller import *


def get_event_by_id(request, event_id):
    events = Event.objects.filter(id=event_id, is_active=True)

    if not len(events):
        json_response = {}

    else:
        event = events[0]
        sessions = Session.objects.filter(event_id=event_id, is_active=True)
        session_array = []

        available_spots_event = 0

        for session in sessions:
            occurrences = Occurrence.objects.filter(session_id=session.id, is_active=True)
            occurrences_array = []
            for occurrence in occurrences:
                occurrences_json = {
                    'room_name': occurrence.room.name,
                    'begin_date_time': occurrence.begin_date_time,
                    'end_date_time': occurrence.end_date_time,
                }
                occurrences_array.append(occurrences_json)

            available_spots_session = session_available_spots(session.id)
            available_spots_event += available_spots_session
            session_json = {
                'instructor_name': session.instructor.name,
                'spots': session.spots,
                'occurrences': occurrences_array,
                'available_spots': available_spots_session,
                'has_spots': available_spots_session > 0,
            }
            # print session_json
            session_array.append(session_json)

        category = Category.objects.get(pk=event.category_id)

        event_category = {'name': category.name, 'image': category.image.url}

        event_json = {
            'category': event_category,
            'edition': event.edition.name,
            'name': event.name,
            'fee': event.fee,
            'workload': event.workload,
            'description': event.description,
            'available_spots': available_spots_event,
            'has_spots': available_spots_event > 0,
            'sessions': session_array,
        }
        json_response = event_json

    return JsonResponse(json_response)


def create_event(request):
    edition_name = request.POST.get('event_edition')
    name = request.POST.get('event_name')
    type = request.POST.get('event_type')
    fee = request.POST.get('event_fee')
    workload = request.POST.get('event_workload')
    description = request.POST.get('description')
    # print edition_name, name, type, fee, workload, description


    context_dict = {
        'cadastro_realizado': "Cadastro realizado com sucesso."
    }
    erros = {}
    event = Event()
    try:
        edition = Edition.objects.get(name=edition_name)
    except Edition.DoesNotExist:
        edition = None
    if edition:
        event.edition = edition
    else:
        erros['edition'] = "Edicao nao encontrada"
    try:
        verify_event_name = Event.objects.get(name=name)
    except Event.DoesNotExist:
        verify_event_name = None
    if name and not verify_event_name:
        event.name = name
    else:
        erros['name'] = "Nome nao preenchido ou duplicado."

    event.type = type

    if fee:
        event.fee = fee
    else:
        event.fee = 0

    if workload:
        event.workload = workload
    else:
        erros['workload'] = "Campo obrigatorio"

    if description:
        event.description = description
    else:
        erros['description'] = "Campo Obrigatorio"

    if not erros:
        event.is_active = True
        event.save()
        editions = Edition.objects.all()
        first_edition = editions[0].name
        context_dict = {
            'title': "Dashboard / Edicao",
            'type': "Cadastro Evento",
            'editions': editions,
            'first_edition': first_edition,
            'cadastro_realizado': "Cadastro realizado com sucesso."
        }
    else:
        editions = Edition.objects.all()
        context_dict = {
            'title': "Dashboard / Edicao",
            'type': "Cadastro Evento",
            'editions': editions,
            'first_edition': edition_name,
            'event_name': name,
            'event_type': type,
            'event_fee': fee,
            'event_workload': workload,
            'event_description': description,
            'erros': erros
        }
    return render(request, 'dashboard/event.html', context=context_dict)


def get_all_events(request):
    events = Event.objects.all()
    events_array = []

    for event in events:
        sessions = Session.objects.filter(event_id=event.id, is_active=True)
        session_array = []
        available_spots_event = 0

        for session in sessions:
            occurrences = Occurrence.objects.filter(session_id=session.id, is_active=True)
            occurrences_array = []
            for occurrence in occurrences:
                occurrences_json = {
                    'room': occurrence.room.number,
                    'begin_date_time': occurrence.begin_date_time,
                    'end_date_time': occurrence.end_date_time,
                }
                occurrences_array.append(occurrences_json)
            session_json = {
                'instructor_name': session.instructor.name,
                'spots': session.spots,
                'occurrences': occurrences_array,
            }
            print session_json
            available_spots_session = session_available_spots(session.id)
            available_spots_event += available_spots_session

            session_array.append(session_json)

        print (event.category.image)
        categorySerializer = CategorySerializer(event.category.image)
        print categorySerializer

        event_json = {
            'category_name': event.category.name,
            'name': event.name,
            'fee': event.fee,
            'workload': event.workload,
            'description': event.description,
            'sessions': session_array,
        }
        events_array.append(event_json)

    events_json = {
        'error': False,
        'events': events_array
    }
    return JsonResponse(events_json)
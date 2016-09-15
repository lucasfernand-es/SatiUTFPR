from sati.models import Event, Edition
from django.shortcuts import render, render_to_response

from django.http import HttpResponseForbidden

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
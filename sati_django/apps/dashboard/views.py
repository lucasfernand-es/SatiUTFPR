from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
# from django.template import RequestContext
# from django.http import HttpResponse
from django.http import HttpResponseForbidden
from sati.models import Event, Edition
from django.template import loader

import json

@login_required
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key title is the same as {{ title }} in the template!
    context_dict = {
        'title': "Dashboard"
    }
    return render(request, 'dashboard/index.html', context=context_dict)

@login_required()
def edition(request):
    if request.user.is_staff:
        context_dict = {
            'title': "Dashboard / Edicao",
            'type': "Cadastro Edicao"
        }
        return render(request, 'dashboard/edition.html', context=context_dict)
    else:
        return HttpResponseForbidden()

@login_required()
def event(request):
    if request.user.is_staff:
        editions = Edition.objects.all()
        first_edition = editions[0].name
        context_dict = {
            'title': "Dashboard / Edicao",
            'type': "Cadastro Evento",
            'editions': editions,
            'first_edition': first_edition
        }
        return render(request, 'dashboard/event.html', context=context_dict)
    else:
        return HttpResponseForbidden()

# def index(request):
#    return HttpResponse("Hello, world. You're at the control panel index.")

# def login(request):
#    return render(
#        request,
#        'sati_utfpr/login.html'
#    )

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from sati.models import Event
from sati.serializers import *
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    print "index"
    return render(request, 'public/index.html')


def login(request):
    print "login"
    print request.user.is_authenticated
    print request.user.username
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html')
    else:
        return render(request, 'public/login.html')


def signup(request):
    return render(request, 'public/signup.html')


def new_login(request):
    return render(request, 'public/login.html')

# Events


def events_list(request):
    return render(request, 'event/index.html')


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    serializer = EventSerializer(event, many=False)
    data = serializer.data
    request.event = data
    request.event_id = event_id

    return render(request, 'event/event_detail.html')
#   return HttpResponse("You're looking at question %s." % event_id)


from django.shortcuts import render, render_to_response, HttpResponse
from django.http import JsonResponse
from rest_framework import serializers
from sati.models import *
from sati_django.sati.serializers import *


def get_public_events(request):

    return JsonResponse('aff')

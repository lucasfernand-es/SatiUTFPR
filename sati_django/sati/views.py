# import os, sys
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, generics, permissions
from sati.models import *
from sati.serializers import *


class EditionList(generics.ListCreateAPIView):
    model = Edition
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class EditionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Edition
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class EventList(generics.ListCreateAPIView):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PersonList(generics.ListCreateAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [
        permissions.AllowAny
    ]

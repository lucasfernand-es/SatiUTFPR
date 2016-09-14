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
        permissions.IsAdminUser
    ]


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]


class SessionList(generics.ListCreateAPIView):
    model = Session
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Session
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class RoomList(generics.ListCreateAPIView):
    model = Room
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Room
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class OccurrenceList(generics.ListCreateAPIView):
    model = Occurrence
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class OccurrenceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Occurrence
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

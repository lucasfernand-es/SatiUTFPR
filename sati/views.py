# import os, sys
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, generics, permissions, authentication
import rest_framework_oauth
from sati.models import *
from sati.serializers import *
from sati.ViewController import authentication as local_authentication


class EditionList(generics.ListCreateAPIView):
    model = Edition
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class EditionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Edition
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class CategoryList(generics.ListCreateAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        #permissions.IsAuthenticated
        permissions.AllowAny
    ]
    #authentication_classes = [
    #    local_authentication.SuperUserSessionAuthentication,
    #]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class EventList(generics.ListCreateAPIView):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class PersonDetailPublic(generics.RetrieveAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PersonList(generics.ListCreateAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Person
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class SessionList(generics.ListCreateAPIView):
    model = Session
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Session
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class RoomList(generics.ListCreateAPIView):
    model = Room
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Room
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class OccurrenceList(generics.ListCreateAPIView):
    model = Occurrence
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class OccurrenceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Occurrence
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class ParticipantList(generics.ListCreateAPIView):
    model = Participant
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]


class ParticipantDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Participant
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        local_authentication.SuperUserSessionAuthentication,
    ]

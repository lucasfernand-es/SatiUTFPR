# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django import forms
from sati.enum import *
from sati.static_variables import *


class Edition(models.Model):
    name = models.CharField(max_length=standard_name_size, unique=True)
    begin_date = models.DateField()
    end_date = models.DateField()
    theme = models.CharField(max_length=150)
    description = models.CharField(max_length=standard_text_field_size)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['begin_date']
        app_label = 'sati'


class Category(models.Model):
    name = models.CharField(max_length=standard_name_size, unique=True)
    image = models.ImageField(default=None)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'sati'


class Event(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.DO_NOTHING, related_name='events', default=None)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='events', default=None)
    name = models.CharField(max_length=standard_name_size, unique=True)
    fee = models.FloatField(default=0.0)
    workload = models.IntegerField(default=0.0)
    description = models.CharField(max_length=standard_text_field_size)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'sati'


class Person(models.Model):
    # user = models.OneToOneField(User) # on_delete=models.CASCADE
    name = models.CharField(max_length=standard_name_size)
    email = models.EmailField(max_length=100,  unique=True)
    password = models.CharField(max_length=32)
    institution = models.CharField(max_length=255, blank=True)
    cpf = models.CharField(max_length=15, unique=True)
    academic_registry = models.CharField(max_length=15, null=True)
    role = models.IntegerField(choices=ROLES, default=3)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'sati'


class Session(models.Model):
    instructor = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='sessions', default=None)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, related_name='sessions', default=None)
    spots = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{0} com {1} - {2} vagas".format(self.instructor.name, self.event.name, self.spots)

    class Meta:
        app_label = 'sati'


class Room(models.Model):
    name = models.CharField(max_length=standard_name_size)
    occupancy = models.IntegerField()
    number = models.IntegerField()
    type = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        app_label = 'sati'


class Occurrence(models.Model):
    begin_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING, related_name='occurrences', default=None)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING,  related_name='occurrences', default=None)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"Occurrence - Session {0} - Room {1}: {2} to {3}"\
            .format(self.session, self.room, self.begin_date_time.date(), self.end_date_time.date())

    class Meta:
        ordering = ['begin_date_time']
        app_label = 'sati'


class Report(models.Model):
    name = models.ForeignKey('Edition', on_delete=models.DO_NOTHING)
    class Meta:
        app_label = 'sati'


class Participant(models.Model):
    person = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    session = models.ForeignKey('Session', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        app_label = 'sati'



class Raffle(models.Model):
    prize = models.CharField(max_length=255)
    raffleDate = models.DateTimeField()
    occurrence = models.ForeignKey(Occurrence, on_delete=models.DO_NOTHING, default=None)
    idParticipant = models.ForeignKey('Participant', on_delete=models.DO_NOTHING, default=None)
    class Meta:
        app_label = 'sati'


class Presence(models.Model):
    entryTime = models.DateTimeField()
    exitTime = models.DateTimeField()
    idParticipant = models.ForeignKey('Participant', on_delete=models.DO_NOTHING, default=None)
    occurrence = models.ForeignKey(Occurrence, on_delete=models.DO_NOTHING, default=None)
    class Meta:
        app_label = 'sati'


class Payment(models.Model):
    type = models.CharField(max_length=30)
    datePayment = models.DateField()
    allowance = models.BooleanField(default=False)
    class Meta:
        app_label = 'sati'



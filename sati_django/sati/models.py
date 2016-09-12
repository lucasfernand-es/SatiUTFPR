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


class Event(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.DO_NOTHING, related_name='events', default=None)
    name = models.CharField(max_length=standard_name_size, unique=True)
    type = models.CharField(max_length=200)
    fee = models.FloatField()
    workload = models.IntegerField()
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
    email = models.CharField(max_length=100,  unique=True)
    password = models.CharField(max_length=32)
    institution = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15, unique=True)
    academicRegistry = models.CharField(max_length=15)
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
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Session: Instructor {0} - Event {1}".format(self.instructor.name, self.event.name)

    class Meta:
        app_label = 'sati'


class Report(models.Model):
    name = models.ForeignKey('Edition', on_delete=models.DO_NOTHING)
    class Meta:
        app_label = 'sati'


class Room(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    space = models.IntegerField()
    type = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    class Meta:
        app_label = 'sati'


class Participant(models.Model):
    person = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    session = models.ForeignKey('Session', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    class Meta:
        app_label = 'sati'


class Ocurrence(models.Model):
    beginTime = models.TimeField()
    endTime = models.TimeField()
    status = models.BooleanField(default=True)
    idSession = models.ForeignKey('Session', on_delete=models.DO_NOTHING)
    idRoom = models.ForeignKey('Room', on_delete=models.DO_NOTHING)
    class Meta:
        app_label = 'sati'


class Raffle(models.Model):
    prize = models.CharField(max_length=255)
    raffleDate = models.DateTimeField()
    idOcurrence = models.ForeignKey('Ocurrence', on_delete=models.DO_NOTHING)
    idParticipant = models.ForeignKey('Participant', on_delete=models.DO_NOTHING)
    class Meta:
        app_label = 'sati'


class Presence(models.Model):
    entryTime = models.DateTimeField()
    exitTime = models.DateTimeField()
    idParticipant = models.ForeignKey('Participant', on_delete=models.DO_NOTHING)
    idOcurrence = models.ForeignKey('Ocurrence', on_delete=models.DO_NOTHING)
    class Meta:
        app_label = 'sati'


class Payment(models.Model):
    type = models.CharField(max_length=30)
    datePayment = models.DateField()
    allowance = models.BooleanField(default=False)
    class Meta:
        app_label = 'sati'



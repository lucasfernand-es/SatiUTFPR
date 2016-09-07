from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=63)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15, unique=True)
    academicRegistry = models.CharField(max_length=15)
    role = models.IntegerField()
    status = models.BooleanField(default=True)

    class Meta:
        app_label = 'sati'


class Edition(models.Model):
    name = models.CharField(max_length=150)
    beginDate = models.DateField()
    endDate = models.DateField()
    status = models.BooleanField(default=True)
    theme = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)

    class Meta:
        app_label = 'sati'


class Report(models.Model):
    name = models.ForeignKey('Edition', on_delete=models.DO_NOTHING)
    class Meta:
        app_label = 'sati'


class Event(models.Model):
    idEdicao = models.ForeignKey('Edition', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    charge = models.FloatField()
    workload = models.IntegerField()
    description = models.CharField(max_length=1000)
    class Meta:
        app_label = 'sati'


class Session(models.Model):
    instructor = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    idEvent = models.ForeignKey('Event', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
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



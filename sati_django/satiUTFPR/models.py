from django.db import models

# Create your models here.


class Person(models.Model):
    password = models.CharField(max_length=63)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    dateBirth = models.DateField()
    cpf = models.CharField(max_length=15, unique=True)
    academicRegistry = models.CharField(max_length=15)
    role = models.IntegerField()
    status = models.BooleanField(default=True)


class Edition(models.Model):
    name = models.CharField(max_length=150)
    beginDate = models.DateField()
    endDate = models.DateField()
    status = models.BooleanField()
    theme = models.CharField(max_length=150)


class Report(models.Model):
    name = models.ForeignKey('Edition', on_delete=models.CASCADE)


class Event(models.Model):
    idEdicao = models.ForeignKey('Edition', on_delete=models.CASCADE)
    status = models.BooleanField()
    type = models.CharField(max_length=200)
    charge = models.FloatField()
    workload = models.IntegerField()


class Session(models.Model):
    instructor = models.ForeignKey('Person', on_delete=models.CASCADE)
    idEvent = models.ForeignKey('Event', on_delete=models.CASCADE)
    status = models.BooleanField()


class Room(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    build = models.CharField(max_length=2)
    space = models.IntegerField()
    type = models.CharField(max_length=30)
    status = models.BooleanField()


class Participant(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)


class Ocurrence(models.Model):
    beginTime = models.TimeField()
    endTime = models.TimeField()
    status = models.BooleanField()
    idSession = models.ForeignKey('Session', on_delete=models.CASCADE)
    idRoom = models.ForeignKey('Room', on_delete=models.CASCADE)


class Raffle(models.Model):
    prize = models.CharField(max_length=255)
    raffleDate = models.DateField()
    idOcurrence = models.ForeignKey('Ocurrence', on_delete=models.CASCADE)
    idParticipant = models.ForeignKey('Participant', on_delete=models.CASCADE)


class Presence(models.Model):
    entryTime = models.DateTimeField()
    exitTime = models.DateTimeField()
    idParticipant = models.ForeignKey('Participant', on_delete=models.DO_NOTHING)
    idOcurrence = models.ForeignKey('Ocurrence', on_delete=models.DO_NOTHING)


class Payment(models.Model):
    type = models.CharField(max_length=30)
    datePayment = models.DateField()



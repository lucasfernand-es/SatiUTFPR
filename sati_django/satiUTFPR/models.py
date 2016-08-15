from django.db import models

# Create your models here.

class Person(models.Model):
    password = models.CharField(max_length=63)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    dateBirth = models.DateField()
    cpf = models.CharField(max_length=15)
    academicRegistry = models.CharField(max_length=15)
    role = models.CharField(max_length=1)
    status = models.BooleanField(default=True)


class Edition(models.Model):
    name = models.CharField(max_length=150)
    beginDate = models.DateField()
    endDate = models.DateField()
    status = models.BooleanField()
    theme = models.CharField(max_length=150)


class Event(models.Model):
    idEdicao = models.ForeignKey('Edition', on_delete=models.CASCADE)
    status = models.BooleanField()
    type = models.CharField(max_length=200)


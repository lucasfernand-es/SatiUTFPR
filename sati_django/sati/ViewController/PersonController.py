from django.shortcuts import render, redirect
from sati_django.sati.models import Person
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def registry_person(request):
    person = Person()
    person.name = request.POST["nome_completo"]
    person.dateBirth = request.POST["data_nascimento"]
    person.institution = request.POST["instituicao"]
    person.password = request.POST["senha"]
    person.cpf = request.POST["cpf"]
    person.email = request.POST["email"]
    person.academicRegistry = request.POST["registro_academico"]
    person.role = 0
    person.status = 1
    person.save()
    return render(
        request,
        'sati_utfpr/test.html'
    )

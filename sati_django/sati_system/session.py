from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

from sati_system.models import Person


def user_authenticate(request):
    print request.POST
    try:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('userpass'))
    except User.DoesNotExist:
        user = None
    return user;


def user_session(request):
    if request.session.get('has_logged', False):
        return True
    else:
        return False


def user_login(request):
    user = Person.objects.get(email=request.POST.get('username'))
    if user.password == request.POST.get('userpass'):
        request.session['has_logged'] = True
        request.session['username'] = user.user.username
        return render(
            request,
            'dashboard/index.html',
        )
    else:
        request.session['has_logged'] = False
        return render(
            request,
            'public/login.html'
        )


def user_logout(request):
    request.session['has_logged'] = False
    request.session['username'] = ""


def user_signup(request):
    person = Person()
    if request.POST["nome_completo"]:
        person.name = request.POST["nome_completo"]

    person.institution = request.POST["instituicao"]
    if request.POST["senha"] == request.POST["confimar_senha"] and request.POST["senha"]:
        person.password = request.POST["senha"]
    else:
        NotImplementedError

    if request.POST["cpf"]:
        person.cpf = request.POST["cpf"]
    else:
        NotImplementedError

    if request.POST["email"]:
        person.email = request.POST["email"]
    else:
        NotImplementedError

    if person.institution and person.institution == "UTFPR":
        person.academicRegistry = request.POST["registro_academico"]
    else:
        NotImplementedError

    # Valores padrao 0 aluno e 1 para ativo
    person.role = 0
    person.status = 1

    # usuario para autenticacao e login
    verify_person_cpf = Person.objects.get(cpf=person.cpf)
    verify_person_email = Person.objects.get(email=person.email)

    if not verify_person_cpf and not verify_person_email:
        user = User()
        user.password = person.password
        user.username = person.email
        user.save()

        person.user = user
        person.save()
    else:
        NotImplementedError

    return render(
        request,
        'sati_utfpr/test.html'
    )

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from sati_django.models import Person


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


def user_signup(request):
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

    # usuario para autenticacao e login
    user = User()
    user.password = person.password
    user.username = person.email
    user.save()

    person.user = user
    person.save()
    return render(
        request,
        'sati_utfpr/test.html'
    )

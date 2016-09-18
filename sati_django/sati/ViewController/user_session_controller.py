from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse

from sati.models import Person


def user_authenticate(username, password):
    print password, username
    user = authenticate(username=username, password=password)
    return user;


def user_session(request):
    if request.session.get('has_logged', False):
        return True
    else:
        return False


def user_login(request):
    user = user_authenticate(request.POST.get('username'), request.POST.get('userpass'))
    if user is not None:
        login(request, user)
        return render(
            request,
            'dashboard/index.html',
        )
    else:
        return render(
            request,
            'public/login.html'
        )


def user_logout(request):
    logout(request)
    return render(request,
                  'public/index.html')


def user_signup(request):

    if request.method == 'POST':
        print 'postou algo'
        print request.body

    print 'chegou aqui'
    return JsonResponse(2, safe=False)
    # return render(
    #    request,
    #    'sati_utfpr/test.html'
    # )
#    if request.POST["nome_completo"]:
#        person.name = request.POST["nome_completo"]
#
#    person.institution = request.POST["instituicao"]
#    if request.POST["senha"] == request.POST.get('confirmar_senha', '') and request.POST["senha"]:
#        person.password = request.POST["senha"]
#    else:
#        NotImplementedError
#
#    if request.POST["cpf"]:
#        person.cpf = request.POST["cpf"]
#    else:
#        NotImplementedError
#
#    if request.POST["email"]:
#        person.email = request.POST["email"]
#    else:
#        NotImplementedError
#
#    if person.institution and person.institution == "UTFPR":
#        person.academicRegistry = request.POST["registro_academico"]
#    else:
#        NotImplementedError
#
#    # Valores padrao 0 aluno e 1 para ativo
#    person.role = 0
#    person.status = 1
#
#    # usuario para autenticacao e login
#    verify_person_cpf = False #Person.objects.get(cpf=person.cpf)
#    verify_person_email = False #Person.objects.get(email=person.email)
#
#    if not verify_person_cpf and not verify_person_email:
#        user = User()
#        user.password = person.password
#        user.username = person.email
#        user.save()
#
#        person.user = user
#        person.save()
#    else:
#        NotImplementedError
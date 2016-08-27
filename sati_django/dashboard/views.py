from django.shortcuts import render, render_to_response
# from django.template import RequestContext
# from django.http import HttpResponse


def index(request):
    return render(request, 'dashboard/index.html')


# def index(request):
#    return HttpResponse("Hello, world. You're at the control panel index.")

# def login(request):
#    return render(
#        request,
#        'sati_utfpr/login.html'
#    )

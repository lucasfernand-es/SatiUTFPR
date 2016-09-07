from django.shortcuts import render, render_to_response
# from django.template import RequestContext
# from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key title is the same as {{ title }} in the template!
    context_dict = {
        'title': "Dashboard"
    }
    return render(request, 'dashboard/index.html', context=context_dict)


def edition(request):
    context_dict = {
        'title': "Dashboard / Edicao"
    }
    return render(request, 'dashboard/edition.html', context=context_dict)



# def index(request):
#    return HttpResponse("Hello, world. You're at the control panel index.")

# def login(request):
#    return render(
#        request,
#        'sati_utfpr/login.html'
#    )

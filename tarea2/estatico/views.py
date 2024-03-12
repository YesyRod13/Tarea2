from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def http_response_view(request):
    return HttpResponse('<ul> <li>Baile</li> <li>Pintura</li> <li>Lectura</li></ul') 

def index(request):
    text = {'lista': "baile, pintura y lectura"}
    return render(request, 'tarea2/index.html', context=text)
    #return HttpResponse("<h1>")

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def novo_evento(request):
    if request.method == "GET":
        return HttpResponse('Novo Evento')

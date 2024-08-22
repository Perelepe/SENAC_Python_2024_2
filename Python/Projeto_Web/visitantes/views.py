from django.shortcuts import render
from django.http import HttpResponse

def registrar_visitantes(request):
    return render(request, "visitantes/visitantes.html")

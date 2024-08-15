from django.shortcuts import render
from django.http import HttpResponse

def visitantes(request):
    return render(request, "visitantes/visitantes.html")

from django.shortcuts import render
from django.http import HttpResponse

def usuarios(request):
    return render(request, "usuarios.html")

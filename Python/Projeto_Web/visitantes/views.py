from django.shortcuts import render
from django.http import HttpResponse
from visitantes.forms import VisitanteForm

def registrar_visitantes(request):
    form = VisitanteForm()
    context = {
        "nome_pagina":"Cadastro de Visitante",
        "form":form,
    }
    return render(request, "visitantes/visitantes.html", context)

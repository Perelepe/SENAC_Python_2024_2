from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from visitantes.forms import ( VisitanteForm, AutorizaVisitanteForm )
from visitantes.models import Visitante

def registrar_visitantes(request):
    form = AutorizaVisitanteForm()

    if request.method == "POST":
        form = AutorizaVisitanteForm(request.POST, instance=visitante)
        if form.is_valid():
            form.save()
            messages.success(request, "Visitante autorizado com sucesso.")
            return redirect("index")

    context = {
        "nome_pagina":"Cadastro de Visitante",
        "form":form,
    }
    return render(request, "visitantes/visitantes.html", context)

def informacoes_visitante(request, id):
    visitante = get_object_or_404(
        Visitante,
        id=id
    )
    context = {
        "nome_pagina": "Informações do Visitante",
        "visitante":visitante,
        }
    return render(request, "informacoes_visitante.html", context)

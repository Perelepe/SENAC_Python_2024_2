from django.shortcuts import render, redirect
from django.http import HttpResponse
from visitantes.forms import VisitanteForm

def registrar_visitantes(request):
    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            visitante = form.save(commit = False)
            visitante.porteiro_autorizador = request.user.porteiro
            visitante.save()
            return redirect("index")

    context = {
        "nome_pagina":"Cadastro de Visitante",
        "form":form,
    }
    return render(request, "visitantes/visitantes.html", context)

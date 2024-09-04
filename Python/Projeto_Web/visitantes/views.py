from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from visitantes.forms import ( VisitanteForm, AutorizaVisitanteForm )
from visitantes.models import Visitante
from porteiros.models import Porteiro

def registrar_visitantes(request):
    form = VisitanteForm(request.POST)

    if form.is_valid():
        visitante = form.save(commit = False)
        visitante.porteiro_autorizador = Porteiro.objects.get(id=1)
        visitante.save()

        messages.sucess(request, "O Visitante foi cadastrado com sucesso!")
        return redirect("index")

    context = {
        "nome_pagina":"Cadastro de Visitante",
        "form":form,
    }
    return render(request, "visitantes/visitantes.html", context)

def informacoes_visitante(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    
    form = AutorizaVisitanteForm()
    if request.method == "POST":
        form = AutorizaVisitanteForm(request.POST, instance=visitante)

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()

            visitante.save()

            messages.success(request, "Visitante autorizado com sucesso.")
        
        return redirect("index")
    
    context = {
        "nome_pagina":"Informações do Visitante",
        "visitante":visitante, 
        "form":form,
    }

    return render(request, "visitantes/informacoes_visitante.html", context)
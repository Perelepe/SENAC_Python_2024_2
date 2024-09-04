from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import registrar_visitantes, informacoes_visitante

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("registrar-visitantes/", registrar_visitantes, name="registrar_visitantes"),
    path("info-visitante/<int:id>", informacoes_visitante, name="informacoes_visitante"),
]

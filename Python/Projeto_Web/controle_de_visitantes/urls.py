from django.contrib import admin
from django.urls import path
from usuarios.views import index
from visitantes.views import registrar_visitantes, informacoes_visitante, finalizar_visita

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="usuarios"),
    path("registrar-visitantes/", registrar_visitantes, name="registrar_visitantes"),
    path("visitantes/<int:id>/", informacoes_visitante, name="informacoes_visitante"),
    path("visitantes/<int:id>/finalizar-visita", finalizar_visita, name="finalizar_visita"
),
]

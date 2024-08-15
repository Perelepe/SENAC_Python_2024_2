from django.contrib import admin
from django.urls import path
from usuarios.views import index
from visitantes.views import visitantes

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="usuarios"),
    path("visitantes/", visitantes, name="lista_visitantes"),
]

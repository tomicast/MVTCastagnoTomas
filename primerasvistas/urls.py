from django.urls import path
from .views import inicio, listado_familiares, agregar_familiares


urlpatterns = [
    path('', inicio),
    path('listado-familiares/', listado_familiares),
    path('agregar-familiares/<nombre>/<dni>/<fecha_nacimiento>/', agregar_familiares),
]
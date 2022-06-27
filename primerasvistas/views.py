

from this import d
from unittest import loader
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

from primerasvistas.models import familiar

def inicio(request):
    return HttpResponse(r'Este es el inicio')

def agregar_familiares(request, nombre, dni, fecha_nacimiento):
   
    template1 = loader.get_template('listado_familiares.html')
    

    Familiar= familiar(nombre = nombre, dni = dni, fecha_nacimiento = fecha_nacimiento) 

    Familiar.save()

    render1 = template1.render({'nombre':nombre, 'dni':dni, 'fecha_nacimiento': fecha_nacimiento})
    return HttpResponse(render1)    

def listado_familiares(request):
    template= loader.get_template('listado_familiares.html')
    lista_familiares = familiar.objects.all()
    render = template.render({'lista_familiares': lista_familiares})
    return HttpResponse(render)
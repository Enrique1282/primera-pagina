from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
import datetime
from django.template import Template,Context

def saludo(request):
    return HttpResponse('<h1 style="font-size: 100px; color: green; background-color: black;">WELCOME</h1>')

def momento(request):
     respuesta = "<h1 style='font-size: 60px; color: green; background-color: black;'>Momento Actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
     return HttpResponse(respuesta)

def lista(request):
     familiares = [
        {"nombre": "Walter", "apellido": "Ibarra", "parentesco": "Padre", "edad": 66},
        {"nombre": "Aida", "apellido": "Acuña", "parentesco": "Madre", "edad": 67},
        {"nombre": "Alejandro", "apellido": "Ibarra", "parentesco": "hermano", "edad": 32},
        {"nombre": "Favio", "apellido": "Ibarra", "parentesco": "hermano", "edad": 35},
        {"nombre": "Marcela","apellido": "Ibarra", "parentesco": "hermana", "edad": 48},
        {"nombre": "Belen","apellido": "Ibarra", "parentesco": "hermana", "edad": 39},
        {"nombre": "Orlando","apellido": "Ibarra", "parentesco": "hermano", "edad": 46},
        {"nombre": "Vicente","apellido": "Ibarra", "parentesco": "yo", "edad": 40},
        {"nombre": "Nahuel","apellido": "Ibarra", "parentesco": "hijo", "edad": 13},
    ]
     return render(request, "lista_familiares.html", {'familiares': familiares})



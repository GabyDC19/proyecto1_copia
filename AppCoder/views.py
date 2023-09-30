from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse ("Hola Mundo, Inicio")

def curso(request):
    return HttpResponse ("Hola Mundo, Hola curso")

def profesores(request):
    return HttpResponse ("Hola Mundo, Hola profesores")

def estudiante(request):
    return HttpResponse ("Hola Mundo, Hola estudiante")

def entregables(request):
    return HttpResponse ("Hola Mundo, entregables")

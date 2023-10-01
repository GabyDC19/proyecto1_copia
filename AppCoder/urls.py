from django.urls import path
from .views import inicio,cursos,profesores, estudiantes, entregables

urlpatterns = [
    path('inicio/', inicio, name= "Inicio"),
    path('cursos/', cursos, name= "Cursos"),
    path('profesores/', profesores, name= "Profesores"),
    path('estudiantes/',estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name= "Entregables")
]

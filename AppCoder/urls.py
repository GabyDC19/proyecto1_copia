from django.urls import path
from .views import inicio,curso,profesores, estudiante, entregables

urlpatterns = [
    path('inicio/', inicio),
    path('curso/', curso),
    path('profesores/', profesores),
    path('estudiante/',estudiante),
    path('entregables/', entregables)
]

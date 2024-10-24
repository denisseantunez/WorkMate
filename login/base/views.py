from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Button


@login_required
def home(request):
    return render(request, "base.html", {})


@login_required
def gestion_tareas(request):
    return render(request, "gestion-tareas.html", {})


@login_required
def gestion_usuarios(request):
    return render(request, "gestion-usuarios.html", {})


@login_required
def crear_nueva_tarea(request):
    return render(request, "crear-nueva-tarea.html", {})


@login_required
def mis_tareas(request):
    return render(request, "mis-tareas.html", {})

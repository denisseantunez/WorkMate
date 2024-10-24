from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gestion-tareas/", views.gestion_tareas, name="gestion_tareas"),
    path("gestion-usuarios/", views.gestion_usuarios, name="gestion_usuarios"),
    path("crear-nueva-tarea/", views.crear_nueva_tarea, name="crear-nueva-tarea"),
    path("mis-tareas/", views.mis_tareas, name="mis-tareas"),
    path("accounts/", include("django.contrib.auth.urls")),
]


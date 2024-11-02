from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from workmates.models import workmateUser
from .form import WorkmateUserCreationForm


@login_required
def home(request):
    return render(request, "base.html", {})


@login_required
def gestion_tareas(request):
    return render(request, "gestion-tareas.html", {})


@login_required
def gestion_usuarios(request):
    users = workmateUser.objects.all()
    print("Users:", users)
    return render(request, "gestion-usuarios.html", {'users', users})



@login_required
def crear_nueva_tarea(request):
    return render(request, "crear-nueva-tarea.html", {})


@login_required
def mis_tareas(request):
    return render(request, "mis-tareas.html", {})

@login_required
def gestion_usuarios(request):
    users = workmateUser.objects.all()  # Fetch all users from the custom model
    return render(request, "gestion-usuarios.html", {'users': users})  # Pass 'users' to the template as a dictionary


@login_required
def gestion_crearusuario(request):
    if request.method == 'POST':
        form = WorkmateUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('base:gestion-usuarios')
    else:
        form = WorkmateUserCreationForm()
    
    return render(request, "gestion-usuarios.html", {'form': form})
@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = WorkmateUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('base:gestion-usuarios') 
    else:
        form = WorkmateUserCreationForm()
    
    return render(request, 'crear-usuario.html', {'form': form})

def editar_usuario(request, user_id):
    user = get_object_or_404(workmateUser, id=user_id)

    if request.method == 'POST':
        form = WorkmateUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('base:gestion-usuarios')
    else:
        form = WorkmateUserCreationForm(instance=user)

    return render(request, 'editar-usuario.html', {'form': form, 'user': user})

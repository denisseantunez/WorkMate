from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from workmates.models import workmateUser
from tasks.models import Tasks
from .form import WorkmateUserCreationForm, WorkmateTaskCreationForm


@login_required
def home(request):
    return render(request, "base.html", {})

@login_required
def gestion_tareas(request):
    tasks = Tasks.objects.all()  # Fetch all tasks

    if request.method == 'POST':
        # Handle the task edit form submission
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Tasks, id=task_id)
        form = WorkmateTaskCreationForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('base:gestion_tareas')

    else:
        form = WorkmateTaskCreationForm()

    return render(request, "gestion-tareas.html", {'tasks': tasks, 'form': form})


@login_required
def crear_nueva_tarea(request):
    return render(request, "crear-nueva-tarea.html", {})


@login_required
def mis_tareas(request):
    mytasks = Tasks.objects.all()
    return render(request, "mis-tareas.html", {'mytasks': mytasks})

@login_required
def gestion_usuarios(request):
    users = workmateUser.objects.all()  
    return render(request, "gestion-usuarios.html", {'users': users})


@login_required
def gestion_crearusuario(request):
    if request.method == 'POST':
        form = WorkmateUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('gestion-usuarios')
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

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = WorkmateTaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully")
            return redirect('base:gestion_tareas')
    else:
        form = WorkmateTaskCreationForm()
    return render(request, 'crear-nueva-tarea.html', {'form': form})

@login_required
def editar_tarea(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    if request.method == 'POST':
        form = WorkmateTaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('gestion_tareas') 
    else:
        form = WorkmateTaskCreationForm(instance=task) 
    return render(request, 'editar-tarea.html', {'form': form, 'task': task})

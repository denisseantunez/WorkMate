from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from workmates.models import workmateUser
from tasks.models import Tasks
from .form import WorkmateUserCreationForm, WorkmateTaskCreationForm


@login_required
def home(request):
    num_tasks = Tasks.objects.count()
    num_team_members = workmateUser.objects.count()
    completed_tasks = Tasks.count_by_progress(Tasks.Completion.Completed)
    in_progress_tasks = Tasks.count_by_progress(Tasks.Completion.Incomplete)
    not_started_tasks = Tasks.count_by_progress(Tasks.Completion.NotStarted)
    return render(request, 'base.html', {
        'num_tasks': num_tasks,
        'num_team_members': num_team_members,
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'not_started_tasks': not_started_tasks,
    })


@login_required
@permission_required('tasks.view_task', raise_exception=True)
def gestion_tareas(request):
    tasks = Tasks.objects.all()

    if request.method == 'POST':
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
@permission_required('tasks.add_task', raise_exception=True)
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
@permission_required('tasks.change_task', raise_exception=True)
def editar_tarea(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = WorkmateTaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('base:gestion_tareas')
    else:
        form = WorkmateTaskCreationForm(instance=task)
    return render(request, 'editar-tarea.html', {'form': form, 'task': task})


@login_required
@permission_required('workmates.view_workmateuser', raise_exception=True)
def gestion_usuarios(request):
    users = workmateUser.objects.all()
    return render(request, "gestion-usuarios.html", {'users': users})


@login_required
@permission_required('workmates.add_workmateuser', raise_exception=True)
def gestion_crearusuario(request):
    if request.method == 'POST':
        form = WorkmateUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect('base:gestion_usuarios')
    else:
        form = WorkmateUserCreationForm()
    return render(request, "crear-usuario.html", {'form': form})


@login_required
@permission_required('workmates.change_workmateuser', raise_exception=True)
def editar_usuario(request, user_id):
    user = get_object_or_404(workmateUser, id=user_id)

    if request.method == 'POST':
        form = WorkmateUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('base:gestion_usuarios')
    else:
        form = WorkmateUserCreationForm(instance=user)

    return render(request, 'editar-usuario.html', {'form': form, 'user': user})


@login_required
def mis_tareas(request):
    filter_category = request.GET.get('category', '')
    filter_priority = request.GET.get('priority', '')
    filter_progress = request.GET.get('progress', '')

    categories = [choice[0] for choice in Tasks.Categories]
    priorities = Tasks.Urgency.choices
    progressing = Tasks.Completion.choices

    mytasks = Tasks.objects.filter(user=request.user)

    if filter_category and filter_category != '':
        mytasks = mytasks.filter(category=filter_category)

    if filter_priority and filter_priority != '':
        mytasks = mytasks.filter(priority=filter_priority)

    if filter_progress and filter_progress != '':
        mytasks = mytasks.filter(progress=filter_progress)

    return render(request, "mis-tareas.html", {
        'mytasks': mytasks,
        'categories': categories,
        'priorities': priorities,
        'progressing': progressing,
        'filter_category': filter_category,
        'filter_priority': filter_priority,
        'filter_progress': filter_progress
    })


@login_required
@permission_required('tasks.add_task', raise_exception=True)
def crear_nueva_tarea(request):
    return render(request, "crear-nueva-tarea.html", {})

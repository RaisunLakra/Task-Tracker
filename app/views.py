from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import TaskForm
from .models import Task

@login_required(login_url='authentication:login')
def tasks(request):
    if request.user.is_authenticated:
        user = request.user
        tasks = Task.objects.filter(user = user).order_by('date')
        return render(request, 'tasks.html', {'tasks': tasks})

@login_required(login_url='authentication:login')
def add_task(request):
    print('add task method called')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully')
            return redirect('app:tasks')
    else:
        form = TaskForm()
        return render(request, 'add-task.html', {'form': form})

@login_required(login_url='authentication:login')
def delete_task(request, task_id):
        Task.objects.get(pk=task_id).delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('app:tasks')

@login_required(login_url='authentication:login')
def update_task(request, task_id):
    pass
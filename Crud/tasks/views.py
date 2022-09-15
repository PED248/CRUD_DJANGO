from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .form import TaskForm
from .models import task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1']
                    )
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'password do no match'})


@login_required
def tasks(request):
    tasks = task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


@login_required
def tasks_completed(request):
    tasks = task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


@login_required
def task_create(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError():
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Please provide valida data'
            })


@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        tasks = get_object_or_404(task, pk=task_id, user=request.user)
        form = TaskForm(instance=tasks)
        return render(request, 'task_detail.html', {
            'task': tasks,
            'form': form
        })
    else:
        try:
            tasks = get_object_or_404(task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=tasks)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': tasks,
                'form': form,
                'error': "Error updating task"
            })


@login_required
def task_save(request, task_id):
    tasks = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST':
        tasks.datecompleted = timezone.now()
        tasks.save()
        return redirect('tasks')


@login_required
def task_delete(request, task_id):
    tasks = get_object_or_404(task, pk=task_id, user=request.user)
    if request.method == 'POST': 
        tasks.delete()
        return redirect('tasks')


@login_required
def sigout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')
        return render(request, 'signin.html', {'form': AuthenticationForm})
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import UserLoginForm
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo_list')  # Redirect to home page after successful login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def home_page(request):
    return render(request, 'home_page.html')




@login_required
def todo_list(request):
    tasks = Task.objects.filter(assigned_to=request.user, completed=False)
    return render(request, 'todo_list.html', {'tasks': tasks})

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.assigned_to == request.user:  # Ensure only assigned user can mark the task as completed
        task.completed = True
        task.save()
    return redirect('todo_list')

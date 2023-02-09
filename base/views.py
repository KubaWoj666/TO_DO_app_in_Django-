from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Task,User
from .forms import TaskForm, UserForm

def welcomePage(request):
    return render(request, 'base/welcome.html', {})


def loginPage(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, f"User dose not exist!")
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, "invalid credentials")

        
    context = {'page':page}
    return render(request, 'base/login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('welcome')


def registerPage(request):
    form = UserForm() 

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")
            
    context = {'form': form}
    return render(request, 'base/login-register.html', context)



def home(request):
    tasks = Task.objects.all()
    users = User.objects.all()
    user_task = Task.objects.filter(host__id = request.user.id, completed = False ).count()
    user_task_completed = Task.objects.filter(host__id = request.user.id, completed = True ).count()
    context = {"tasks":tasks, "users":users, "user_task":user_task, "user_task_completed":user_task_completed  }
    return render(request, 'base/home.html', context)


def task(request, pk):
    task = Task.objects.get(id=pk)
    context = {"task": task}
    return render(request, "base/task.html", context)


def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.host = request.user
        task.save()
        return redirect('home')
    context = {"form": form}
    return render(request, 'base/add-task.html', context)    


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form  = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('home')
    context = {'task': task, 'form': form}
    return render(request, 'base/add-task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    
    context = {'obj': task}
    return render(request, 'base/delete.html', context)

def completed_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.completed = True
        task.save()
        return redirect('home')
    context = {'task':task, "obj":task}
    return render(request, "base/completed-task.html", context)
    








    



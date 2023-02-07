from django.shortcuts import render, redirect


from .models import Task
from .forms import TaskForm



def home(request):
    tasks = Task.objects.all()
    context = {"tasks":tasks}
    return render(request, 'base/home.html', context)


def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}
    return render(request, 'base/add-task.html', context)    

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form  = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # task.name = request.POST.get('name')
            # task.description = request.POST.get('description')
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







    



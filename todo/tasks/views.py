from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    params = {
        'tasks':tasks,
        'form':form,
    } 
    return render(request,'tasks/list.html',params)

def updateTask(request,pk):
    task  = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    params = {
        'form':form,
    }
    return render(request,'tasks/update_task.html',params)

def delete(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("/")

    params = {
        'item':item
    }
    return render(request,'tasks/delete.html',params)
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.
def addtask(request):
    todos = Todo.objects.all()
    if request.method == "POST":
        task=request.POST.get('task')
        if task:
            Todo.objects.create(task=task)
            return redirect('remTask')

    return render(request, 'index.html',{'todos': todos})
def remTask(request):
    todos = Todo.objects.all()

    if request.method == "POST":
        selected_tasks = request.POST.getlist('task')
        
        if selected_tasks:
            Todo.objects.filter(task__in=selected_tasks).delete()
            return redirect('remTask')

    return render(request, 'base2.html', {"todos": todos})


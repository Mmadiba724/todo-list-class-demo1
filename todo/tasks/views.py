from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Tasks
from datetime import datetime
# Create your views here.
# Create view functions for Adding, Editing, Reading and Deleting. (CRUD)

def taskHome(request):
    all_tasks = Tasks.objects.all()
    context = {
        'all_tasks': all_tasks
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context))

def addTask(request):
    message = None
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        task = Tasks(title=title, content=content)
        task.save()
        message = "Task Added Successfully"
    context = {
        'message': message
    }
    return HttpResponse(loader.get_template('add.html').render(context))

def readTask(request, id):
    my_tasks = Tasks.objects.get(id=id)
    context = {
       'task': my_tasks
    }
    template = loader.get_template('viewtask.html')
    return HttpResponse(template.render(context))

def deleteTask(request, id):
    Tasks.objects.filter(id=id).delete()
    return redirect('/')

def editTask(request, id):
    time_now = datetime.now()
    my_task = Tasks.objects.get(id=id)
    my_task_status = my_task.status
    if my_task_status == 0:
        # This means that the task is pending.
        Tasks.objects.filter(id=id).update(status=1, date=time_now)
    elif my_task_status == 1:
        Tasks.objects.filter(id=id).update(status=0, date=time_now)
    return redirect('/read/'+str(id))

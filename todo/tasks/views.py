from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tasks
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
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        task = Tasks(title=title, content=content)
        task.save()
    return HttpResponse(loader.get_template('add.html').render())

def editTask(request, id):
    return HttpResponse("EditTask")

def readTask(request, id):
    # /read/:id number
    my_id = id
    my_tasks = Tasks.objects.get(id=my_id)
    context = {
       'task': my_tasks
    }
    template = loader.get_template('viewtask.html')
    return HttpResponse(template.render(context))

    

def deleteTask(request, id):
    return HttpResponse("DeleteTask")
from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404, redirect

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todo/task_list.html", {"tasks": tasks})

def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect("task_list")
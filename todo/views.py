from django.shortcuts import render
from .models import Task
from django.shortcuts import get_object_or_404, redirect

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todo/task_list.html", {"tasks": tasks})

def task_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    return render(request, "todo/task_add.html")

def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect("task_list")

def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.is_completed = "is_completed" in request.POST
        task.save()
        return redirect("task_list")
    return render(request, "todo/task_edit.html", {"task": task})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "todo/task_delete.html", {"task": task})
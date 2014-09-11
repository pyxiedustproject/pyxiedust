from django.shortcuts import render

from .models import Task

def task_list_all(request):
    tasks = Task.objects.all()
    return render(request,
        'tasks/list_all.html',
        {'tasks': tasks}
    )


def task_list_todo(request):
    tasks = Task.objects.filter(done=False)
    return render(request,
        'tasks/list_todo.html',
        {'tasks': tasks}
    )

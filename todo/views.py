from django.shortcuts import render, redirect
from .models import Task

#for task list 
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        # Check if a task with the same title already exists
        if not Task.objects.filter(title=title).exists():
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')


# for edit the task
def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'task': task})

# for delete the task
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/delete_task.html', {'task': task})

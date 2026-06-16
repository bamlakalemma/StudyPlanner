from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudyTask
from .forms import StudyTaskForm
from django.shortcuts import render, redirect
# Create your views here.

@login_required
def StudyTaskListView(request):
    tasks = StudyTask.objects.filter(owner=request.user)
    return render(request, 'planner.html', {'tasks': tasks})


@login_required
def add_studytask(request):
    if request.method == 'POST':
        form = StudyTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('planner')
    else:
        form = StudyTaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def edit_studytask(request, task_id):
    task = StudyTask.objects.get(id=task_id, owner=request.user)
    
    if request.method == 'POST':
        form = StudyTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('planner')
    else:
        form = StudyTaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'task': task, 'form': form})

@login_required
def delete_studytask(request, task_id):
    task = StudyTask.objects.get(id=task_id, owner=request.user)
    
    if request.method == 'POST':
        task.delete()
        return redirect('planner')
    
    return render(request, 'tasks/delete_task.html', {'task': task})
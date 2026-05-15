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
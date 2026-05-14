from django.shortcuts import render
from django.views.generic import ListView
from .models import StudyTask
from .forms import StudyTaskForm
from django.shortcuts import render, redirect
# Create your views here.

class StudyTaskListView(ListView):
    model = StudyTask
    template_name = 'planner.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return StudyTask.objects.all()

def add_studytask(request):
    if request.method == 'POST':
        form = StudyTaskForm(request.POST)
        if form.is_valid():
            # form.save()
            c = form.save(commit=False)
            c.owner_id = 1
            c.save()
            return redirect('planner')
    else:
        form = StudyTaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})
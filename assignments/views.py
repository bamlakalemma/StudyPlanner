from django.views.generic import ListView
from .models import Assignment
from .forms import AssignmentForm
from django.shortcuts import render, redirect 
# Create your views here.

class assignmentsView(ListView):
    model = Assignment
    template_name = 'assignments.html'
    context_object_name = 'assignments'

    def get_queryset(self):
        return Assignment.objects.all().order_by('due_date')

def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.owner_id = 1
            c.save()
            return redirect('assignments')
    else:
        form = AssignmentForm()
    return render(request, 'assignments/add_assignment.html', {'form': form})
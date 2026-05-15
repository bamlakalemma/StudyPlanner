from django.contrib.auth.decorators import login_required
from .models import Assignment
from .forms import AssignmentForm
from django.shortcuts import render, redirect 
# Create your views here.

# class assignmentsView(ListView):
#     model = Assignment
#     template_name = 'assignments.html'
#     context_object_name = 'assignments'

#     def get_queryset(self):
#         return Assignment.objects.all().order_by('due_date')

@login_required
def assignmentsView(request):
    assignments = Assignment.objects.filter(owner=request.user)
    return render(request, 'assignments.html', {'assignments': assignments})

@login_required
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.owner = request.user
            assignment.save()
            return redirect('assignments')
    else:
        form = AssignmentForm()
    return render(request, 'assignments/add_assignment.html', {'form': form})
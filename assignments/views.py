from django.contrib.auth.decorators import login_required
from .models import Assignment
from .forms import AssignmentForm
from django.shortcuts import render, redirect 
# Create your views here.


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

@login_required
def edit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id, owner=request.user)
    
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignments')
    else:
        form = AssignmentForm(instance=assignment)
    
    return render(request, 'assignments/edit_assignment.html', {'assignment': assignment, 'form': form})

@login_required
def delete_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id, owner=request.user)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignments')
    return render(request, 'assignments/delete_assignment.html', {'assignment': assignment})
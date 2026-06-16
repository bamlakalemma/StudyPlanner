from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CourseForm
from .models import Course
# Create your views here.


@login_required
def coursesListView(request):
    courses = Course.objects.filter(owner=request.user)
    return render(request, 'courses.html', {'courses': courses})

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user
            course.save()
            return redirect('courses')
    else:
        form = CourseForm()
    
    return render(request, 'courses/add_course.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = Course.objects.get(id=course_id, owner=request.user)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})

@login_required
def delete_course(request, course_id):
    course = Course.objects.get(id=course_id, owner=request.user)
    
    if request.method == 'POST':
        course.delete()
        return redirect('courses')
    
    return render(request, 'courses/delete_course.html', {'course': course})
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
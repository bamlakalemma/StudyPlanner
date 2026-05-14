from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import CourseForm
from .models import Course
# Create your views here.

class coursesListView(ListView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            # form.save()
            c = form.save(commit=False)
            c.owner_id = 1 
            c.save()
            return redirect('courses')
    else:
        form = CourseForm()
    
    return render(request, 'courses/add_course.html', {'form': form})
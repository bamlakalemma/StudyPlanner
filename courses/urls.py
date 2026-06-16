from django.urls import path
from .views import coursesListView, add_course, edit_course, delete_course

urlpatterns = [
    path('', coursesListView, name='courses'),
    path('add/', add_course, name='add_course'),
    path('edit/<int:course_id>/', edit_course, name='edit_course'),
    path('delete/<int:course_id>/', delete_course, name='delete_course'),
]
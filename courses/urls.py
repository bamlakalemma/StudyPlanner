from django.urls import path
from .views import coursesListView, add_course

urlpatterns = [
    path('', coursesListView, name='courses'),
    path('add/', add_course, name='add_course'),
]
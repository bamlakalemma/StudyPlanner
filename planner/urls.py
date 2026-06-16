from django.urls import path 
from .views import StudyTaskListView, add_studytask, delete_studytask, edit_studytask

urlpatterns = [
    path('', StudyTaskListView, name='planner'), 
    path('add/', add_studytask, name='add_task'),
    path('edit/<int:task_id>/', edit_studytask, name='edit_task'),
    path('delete/<int:task_id>/', delete_studytask, name='delete_task'),
]


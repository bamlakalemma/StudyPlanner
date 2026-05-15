from django.urls import path 
from .views import StudyTaskListView, add_studytask

urlpatterns = [
    path('', StudyTaskListView, name='planner'), 
     path('add/', add_studytask, name='add_task'),
]


from django.urls import path
from .views import add_assignment, assignmentsView, delete_assignment

urlpatterns = [
    path('', assignmentsView, name='assignments'),
    path('add/', add_assignment, name='add_assignment'),
    path('edit/<int:assignment_id>/', add_assignment, name='edit_assignment'),
    path('delete/<int:assignment_id>/', delete_assignment, name='delete_assignment'),
     
      
]
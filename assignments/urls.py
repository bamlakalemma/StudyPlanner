from django.urls import path
from .views import add_assignment, assignmentsView

urlpatterns = [
    path('', assignmentsView, name='assignments'),
     path('add/', add_assignment, name='add_assignment'),
      
]
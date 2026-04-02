from django.urls import path, include
from .views import AssignmentHomeView

urlpatterns =[
  path('', AssignmentHomeView.as_view(), name='assignment_home')
]
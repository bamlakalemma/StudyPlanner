from django.urls import path 
from . import views

urlpatterns = [
    path('', views.profileListView.as_view(), name='profiles'),  
]
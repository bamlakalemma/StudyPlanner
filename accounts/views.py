from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.

class profileListView(ListView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all()
from django.shortcuts import render, redirect 
from .models import Profile
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profileListView(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})



def signup_view(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})
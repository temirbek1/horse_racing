from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, HorseForm
from .models import Horse
from django.contrib.auth.decorators import login_required

def home(request):
    horses = Horse.objects.all()
    return render(request, 'home.html', {'horses': horses})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    user_horses = Horse.objects.filter(owner=request.user)
    return render(request, 'profile.html', {'horses': user_horses})

@login_required
def add_horse(request):
    if request.method == 'POST':
        form = HorseForm(request.POST)
        if form.is_valid():
            horse = form.save(commit=False)
            horse.owner = request.user
            horse.save()
            return redirect('profile')
    else:
        form = HorseForm()
    return render(request, 'add_horse.html', {'form': form})

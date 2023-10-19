from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def aboutUs(request):
    return render(request, 'aboutUs.html', {})

def contactUs(request):
    return render(request, 'contactUs.html', {})


def viewer(request):
    return render(request, 'viewer.html', {})

def login_user(request):
    login(request)
    messages.success(request, "You have been logged in.")
    return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully, Welcome!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.error(request, "Error logging in. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
    return render(request, 'home.html', {})

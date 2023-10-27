from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addfurnitureform
from .models import Categorie, Product
from django import forms


# Create your views here.
def viewer(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'viewer.html', context)

def aboutUs(request):
    return render(request, 'aboutUs.html', {})

def contactUs(request):
    return render(request, 'contactUs.html', {})

def login_user(request):
    login(request)
    messages.success(request, "You have been logged in.")
    return redirect('home')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


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


def addProduct(request):
    if request.method == 'POST':
        form = addfurnitureform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the 'home' view
    else:
        form = addfurnitureform()
    return render(request, 'adder.html', {'form': form})


def category_products_view(request, category_name):
    category = Categorie.objects.get(name=category_name)
    products = Product.objects.filter(catagory=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})

def rugs_view(request):
    return redirect('category_products', category_name='Rugs')

def misc_view(request):
    return render(request, 'pages/misc.html')

def wall_covering_view(request):
    return render(request, 'pages/wallcoverings.html')

def mirror_view(request):
    return render(request, 'pages/mirror.html')

def fireplace_view(request):
    return render(request, 'pages/fireplace.html')

def paint_view(request):
    return render(request, 'pages/paint.html')

def moulding_view(request):
    return render(request, 'pages/moulding.html')

def doors_view(request):
    return render(request, 'pages/doors.html')

def plumbing_view(request):
    return render(request, 'pages/plumbing.html')

def floral_view(request):
    return render(request, 'pages/floral.html')

def seasonal_view(request):
    return render(request, 'pages/seasonal.html')

def decor_view(request):
    return render(request, 'pages/decor.html')

def textiles_view(request):
    return render(request, 'pages/textiles.html')

def fine_art_view(request):
    return render(request, 'pages/fine-art.html')

def flooring_view(request):
    return render(request, 'pages/flooring.html')

def tile_view(request):
    return render(request, 'pages/tile.html')

def hardware_view(request):
    return render(request, 'pages/hardware.html')

def lighting_view(request):
    return render(request, 'pages/lighting.html')

def sofa_view(request):
    return render(request, 'pages/sofa.html')

def bed_view(request):
    return render(request, 'pages/bed.html')

def table_view(request):
    return render(request, 'pages/table.html')

def painting_view(request):
    return render(request, 'pages/painting.html')

def bench_view(request):
    return render(request, 'pages/bench.html')

def chair_view(request):
    return render(request, 'pages/chair.html')
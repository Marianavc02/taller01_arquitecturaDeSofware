from django.shortcuts import render
from django.http import HttpResponse
from .models import AuthorizedPersonnel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


from django.shortcuts import get_object_or_404, redirect

# Vista de inicio, donde rediriges si el usuario no está autenticado
@login_required
def home(request):
    # Verifica si el usuario está autenticado y es un admin
    is_admin = request.user.groups.filter(name='admin').exists()
    
    # Pasa la variable 'is_admin' al contexto
    return render(request, 'home.html', {'is_admin': is_admin})

@login_required
def admin_only_view(request):
    if not request.user.is_superuser:
        return redirect('home')  # O la página que quieras redirigir
    return render(request, 'admin_only_page.html')


def personnel(request):
    personal = AuthorizedPersonnel.objects.all()
    return render(request, 'personnel.html', {'personal': personal})


def es_admin(user):
    return user.is_superuser or user.groups.filter(name='admin').exists()


def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'registrar.html', {'error': 'The user already exists'})
        
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'User successfully registered')  
        return redirect('home')
    
    return render(request, 'registrar.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar usuario
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            # Redirigir al dashboard adecuado según el rol
            if user.is_staff:
                return redirect('home')  # Admin Dashboard
            else:
                return redirect('home')  # User Dashboard
        else:
            messages.error(request, "Incorrect username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect(reverse('landing'))  # Redirige a la página de login


@login_required
@user_passes_test(es_admin)
def admin_users_view(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'admin_users.html', {'users': users})

@login_required
@user_passes_test(es_admin)
def delete_user_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, 'User successfully deleted.')
    except User.DoesNotExist:
        messages.error(request, 'The user does not exist.')
    
    return redirect('admin_users')


def landing_page(request):
    return render(request, 'landing.html')
from django.shortcuts import redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('home')  # Usuario autenticado -> Dashboard
    else:
        return redirect('landing')  # Usuario no autenticado -> Landing page


def about(request):
    return render(request, 'about.html')




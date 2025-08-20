from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm, LoginForm
from .models import Usuario

from django.contrib.auth import login
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            login(request, usuario)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    usuarios = Usuario.objects.all()
    return render(request, 'dashboard.html', {'usuarios': usuarios})

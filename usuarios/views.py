from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm, LoginForm, EditarUsuarioForm

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

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista.html', {'usuarios': usuarios})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista')
    return render(request, 'eliminar.html', {'usuario': usuario})


def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    form = EditarUsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'editar.html', {'form': form})



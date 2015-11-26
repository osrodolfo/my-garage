from django.shortcuts import render
from django.utils import timezone
from .models import Registro
from django.shortcuts import render, get_object_or_404
from .forms import RegistroForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

def Listar(request):
    dato = Registro.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'garage/Listar_carros.html', {'dato':dato})

def Detalles(request, pk):
    dato = get_object_or_404(Registro, pk=pk)
    return render(request, 'garage/detalle_carro.html', {'dato': dato})

def Nuevo(request):
    if request.method == "POST":
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.save()
            return redirect('garage.views.Detalles', pk=form.pk)
    else:
        form = RegistroForm()
    return render(request, 'garage/editar_carro.html', {'form': form})

def Editar(request, pk):
        dato = get_object_or_404(Registro, pk=pk)
        if request.method == "POST":
            form = RegistroForm(request.POST, request.FILES,instance=dato)
            if form.is_valid():
                form = form.save(commit=False)
                form.usuario = request.user
                form.save()
                return redirect('garage.views.Detalles', pk=form.pk)
        else:
            form = RegistroForm(instance=dato)
        return render(request, 'garage/editar_carro.html', {'form': form})

def Eliminar(request, pk):
        dato = get_object_or_404(Registro, pk=pk)
        if request.method == "POST":
            dato.delete()
            return redirect('garage.views.Listar')
        return render(request, 'garage/eliminar_carro.html', {'dato': dato})

def Login(request):
    mensaje=None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('garage.views.Listar')
                else:
                    mensaje ='tu usuario esta inactivo'
            else:
                mensaje ='usuario o password son incorrectos'
    else:
        form = LoginForm()
    return render(request, 'garage/login.html', {'mensaje' : mensaje, 'form':form})

def Logout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('garage.views.Login')

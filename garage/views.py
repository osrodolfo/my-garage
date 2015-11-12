from django.shortcuts import render
from django.utils import timezone
from .models import Registro
from django.shortcuts import render, get_object_or_404
from .forms import RegistroForm
from django.shortcuts import redirect

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
                form.user = request.user
                form.save()
                return redirect('garage.views.Detalles', pk=form.pk)
        else:
            form = RegistroForm(instance=dato)
        return render(request, 'garage/editar_carro.html', {'form': form})

def Eliminar(request, pk):
        dato = get_object_or_404(Registro, pk=pk)
        if request.method == "POST":
            form = RegistroForm(request.POST, request.FILES,instance=dato)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('garage.views.Detalles', pk=form.pk)
        else:
            form = RegistroForm(instance=dato)
        return render(request, 'garage/editar_carro.html', {'form': form})

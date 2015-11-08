from django.shortcuts import render
from django.utils import timezone
from .models import Registro
from django.shortcuts import render, get_object_or_404

def Listar(request):
    dato = Registro.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'garage/Listar_carros.html', {'dato':dato})

def Detalles(request, pk):
        dato = get_object_or_404(Registro, pk=pk)
        return render(request, 'garage/detalle_carro.html', {'dato': dato})

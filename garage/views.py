from django.shortcuts import render

def Listar(request):
        return render(request, 'garage/Listar_carros.html', {})

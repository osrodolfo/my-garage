from django.shortcuts import render
from django.utils import timezone
from .models import Registro
from django.shortcuts import render, get_object_or_404
from .forms import RegistroForm, LoginForm, RegistroUserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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

def RegistroUser(request):
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = RegistroUserForm(request.POST)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            # E instanciamos un objeto User, con el username y password
            user = User.objects.create_user(username=username, password=password)
            # Y guardamos el objeto, esto guardara los datos en la db.
            user.save()
            return redirect('garage.views.Login')
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = RegistroUserForm()
    # Creamos el contexto
    context = {'form': form}
    return render(request, 'garage/registrar.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, PaisForm, TiendaForm, EventoForm
from django.contrib import messages
from .models import RegisteredUser, Pais, Tienda, Evento
from django.core.exceptions import ObjectDoesNotExist 


def app_homepage(request):
    try:
        if usrnme:
            userdetails = {'username': usrnme}
            return render(request, "loggedin.html", userdetails)
    except NameError:
        return render(request, 'homepage.html')

def about_us(request):
    try:
        if usrnme:
            return render(request, 'aboutUs.html')
    except NameError:
        return render(request, 'aboutUs.html')


def services(request):
    try:
        if usrnme:
           return render(request, 'services.html')
    except NameError:
        return render(request, 'services.html')


def contact_us(request):
    try:
        if usrnme:
           return render(request, 'contactUs.html')
    except NameError:
        return render(request, 'contactUs.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitósamente")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)
    
# def signin(request):
#     return render(request, 'signin.html')


# Creación de la vista sign-in
def signin(request):
    global usrnme
    if request.method == 'POST':
        usrnme = request.POST['username']
        psswrd = request.POST['pswd']
        
        try:
            user = RegisteredUser.objects.get(name=usrnme)
            if usrnme == user.name and psswrd == user.password:
                return redirect('loggedin')
            else:
                messages.info(request, "Clave incorrecta")
                return redirect("signin")
        except ObjectDoesNotExist:
            messages.info(request, "El usuario no existe")
            return redirect("signin")
    else:
        return render(request, "signin.html")
    
    
def loggedin(request):
    userdetails = {'username': usrnme}
    return render(request, "loggedin.html", userdetails)

def logout(request):
    global usrnme
    del usrnme
    return render(request, "logout.html")


def pais(request):
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "País creado exitósamente")
            return redirect("registrarpais")
    else:
        form = PaisForm()
        user_info = {'form': form}
        return render(request, "registerpais.html", user_info)
    
    
def tienda(request):
    if request.method == "POST":
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tienda creada exitósamente")
            return redirect("registrartienda")
    else:
        form = TiendaForm()
        user_info = {'form': form}
        return render(request, "registertienda.html", user_info)

def evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento creado exitósamente")
            return redirect("registrarevento")
    else:
        form = EventoForm()
        user_info = {'form': form}
        return render(request, "registerevento.html", user_info)
    
    
def registrados(request):
    clientes = RegisteredUser.objects.all()
    return render(request, "registrados.html", {"clientes": clientes})

def eventosagendados(request):
    eventos_agendados = Evento.objects.all()
    return render(request, "eventosagendados.html", {"eventos_agendados": eventos_agendados})

def tiendas_registradas(request):
    tiendas = Tienda.objects.all()
    return render(request, "tiendas_registradas.html", {"tiendas": tiendas})
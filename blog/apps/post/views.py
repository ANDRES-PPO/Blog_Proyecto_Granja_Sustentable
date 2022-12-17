from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm, RegistroForm

from django.contrib.auth.models import User
from django.views.generic import View, CreateView
from django.contrib import messages

from django.contrib.admin.views.decorators import staff_member_required  # Import para el create requerir que el usuario sea parte del staff (administrador)

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def quienes_somos(request):
	return render(request, "quienes-somos.html", {})

def proyectos(request):
	return render(request, "proyectos.html", {})

def servicios(request):
	return render(request, "servicios.html", {})

def publicaciones(request):
	return render(request, "publicaciones.html", {})

def areas_de_estudio(request):
	return render(request, "areas-de-estudio.html", {})

def crear_post(request):
	return render(request, "crear-post.html", {})

#Vista para crear un posteo

@staff_member_required          # Requiere que el usuario sea parte del staff (administrador)
def crear_post(request):
    
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('crear_post')
    else:
        post_form = PostForm()
    return render(request, 'crear-post.html', {'post_form': post_form})


#Vista para crear un posteo

def registroUsuario(request):
    if request.method == 'POST':
        registro_form = RegistroForm(request.POST or None, request.FILES or None)
        if registro_form.is_valid():
            registro_form.save()
            return redirect('home')
    else:
        registro_form = RegistroForm()

    context = {
        'registro_form': registro_form,
    }
    return render(request, 'registration/registro_usuario.html', context)



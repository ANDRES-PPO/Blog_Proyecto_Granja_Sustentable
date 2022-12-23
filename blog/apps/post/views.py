from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm, RegistroForm

from django.contrib.auth.models import User
from django.views.generic import View, CreateView
from django.contrib import messages
from django.urls import reverse_lazy

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
   
def areas_de_estudio(request):
	return render(request, "areas-de-estudio.html", {})

#Vista para Mostrar y Filtrar Posteos

class publicaciones(View):
    template_name = 'publicaciones.html'

    def get(self, request):
        posteos = Post.objects.all().order_by('-fecha_creacion')
        categorias = Categoria.objects.all()
        context = {
           'posteos': posteos,
           'categorias': categorias
        }
        return render(request, self.template_name, context)

    def post(self, request):
        categorias = Categoria.objects.all()
        cate = request.POST.get('categoria', None)
        fecha = request.POST.get('fecha', None)

        if cate == "Todas" and fecha:
            posteos = Post.objects.filter(fecha_creacion=fecha).order_by('-fecha_creacion')
           
        elif cate and fecha:
            posteos = Post.objects.filter(categoria__nombre=cate, fecha_creacion=fecha).order_by('-fecha_creacion')
        elif cate:
            if cate == "Todas":
                posteos = Post.objects.all().order_by('-fecha_creacion')
            else:
                posteos = Post.objects.filter(categoria__nombre=cate).order_by('-fecha_creacion')
        elif fecha:
            posteos = Post.objects.filter(fecha_creacion=fecha).order_by('-fecha_creacion')
        context = {
           'posteos': posteos,
           'categorias': categorias
        }
        return render(request, self.template_name, context)

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

#Vista para Ver un solo posteo

def ver_post(request, id):
    if request.method=='GET':
        posteo = Post.objects.get(id=id)
        posteo.visitas += 1                                         #Incrementa el conteo de visitas
        Post.objects.filter(id=id).update(visitas=posteo.visitas)   #Actualiza la bd las visitas
        context = { 'posteo': posteo}
    return render(request, 'post/post.html', context)

#Vista para registrar un usuario

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



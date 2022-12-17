from django.contrib import admin
from .models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('id', 'nombre', 'activado', 'fecha_creacion')
    search_fields = ('id', 'nombre', 'activado', 'fecha_creacion')
    list_display = ('id', 'nombre', 'activado', 'fecha_creacion')
    list_filter = ('activado',)

class PostAdmin(admin.ModelAdmin):
    ordering = ('id', 'titulo', 'resumen', 'texto', 'imagen', 'categoria', 'publicado', 'fecha_creacion', 'usuario')
    search_fields = ('id', 'titulo', 'resumen', 'texto', 'imagen', 'categoria__nombre', 'publicado', 'fecha_creacion')
    list_display = ('titulo', 'resumen', 'imagen', 'categoria', 'publicado', 'fecha_creacion', 'usuario')
    list_filter = ('categoria__nombre', 'publicado')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

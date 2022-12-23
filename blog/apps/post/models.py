from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    activado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural ='Categorias'
        
    def __str__(self) :
        return str(self.nombre)
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40, blank=False, null=False)
    resumen = models.CharField(max_length=300, blank=False, null=False)
    texto = models.TextField(max_length=1500, blank=False, null=False)
    imagen = models.ImageField(upload_to='post', null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'posts')
    visitas = models.IntegerField(default=True)
    
    class Meta:
        verbose_name_plural = 'Posteos'
        ordering = ['fecha_creacion']  # ordena por fecha de creacion
    
    def __str__(self) :
        return str(self.titulo)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField(max_length=180, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)


    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self) :
        return str(self.texto)

    
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.post.views import *
from django.views.generic.base import TemplateView # agregado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('quienes-somos/', quienes_somos, name='quienes_somos'),
    path('proyectos/', proyectos, name='proyectos'),
    path('servicios/', servicios, name='servicios'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('areas-de-estudio/', areas_de_estudio, name='areas_de_estudio'),
    path('crear-post', crear_post, name='crear_post'),

    path('registro/', registroUsuario, name='registro'), #agregado
    path('accounts/', include('django.contrib.auth.urls')), #agregado
    path('', TemplateView.as_view(template_name='home.html'), name='home'), #agregado
]
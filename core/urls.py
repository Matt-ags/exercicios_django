"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from medico import views
from medico.views import registrar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
    path('deletar_especialidade/<int:id>/', views.deletar_especialidade, name='deletar_especialidade'),
    path('add_medico/', views.add_medico, name='add_medico'),
    path('add_especialidade/', views.add_especialidade, name='add_especialidade'),
    path('editar_especialidade/<int:id>/', views.editar_especialidade, name='editar_especialidade'),
    path('editar_medico/<int:id>/', views.editar_medico, name='editar_medico'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', registrar_usuario, name='register'),

]

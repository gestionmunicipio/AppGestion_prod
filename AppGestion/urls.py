"""AppGestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from panel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('diagnostico/', views.diagnostico, name="diagnostico"),
    path('personas/', views.personas, name="personas"),
    path('cultura/', views.cultura, name="cultura"),
    path('liderazgo/', views.liderazgo, name="liderazgo"),
    path('estrategia/', views.estrategia, name="estrategia"),
    path('estructura/', views.estructura, name="estructura"),
    path('operaciones/', views.operaciones, name="operaciones"),
    path('creatividad/', views.creatividad, name="creatividad"),
    path('tecnologia/', views.tecnologia, name="tecnologia"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('resumen/', views.resumen, name="resumen")
]

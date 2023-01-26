"""project_name URL Configuration

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
from django.urls import path


from crud.views import ProductosListado, ProductoDetalle, ProductoCrear, ProductoActualizar, ProductoEliminar



urlpatterns = [
    path('admin/', admin.site.urls),
    # La ruta 'leer' en donde listamos todos los registros o productos de la Base de Datos
    path('productos/', ProductosListado.as_view(template_name = "productos/index.html"), name='leer'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo producto o registro  
    path('productos/crear', ProductoCrear.as_view(template_name = "productos/crear.html"), name='crear'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('productos/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "productos/detalles.html"), name='detalles'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('productos/editar/<int:pk>', ProductoActualizar.as_view(template_name = "productos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('productos/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminar'),    

]

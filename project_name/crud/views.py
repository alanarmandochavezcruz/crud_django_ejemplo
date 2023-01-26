from django.shortcuts import render


# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Productos' para poder usarlo en nuestras Vistas CRUD
from .models import Productos

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms




class ProductosListado(ListView): 
    model = Productos
 
class ProductoDetalle(DetailView): 
    model = Productos
 
class ProductoCrear(SuccessMessageMixin, CreateView): 
    model = Productos
    form = Productos
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Producto     
 
    # Redireccionamos a la página principal luego de crear un registro o Producto
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Productos
    form = Productos
    fields = "__all__"  
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
 
    # Redireccionamos a la página principal luego de actualizar un registro o Producto
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Productos 
    form = Productos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
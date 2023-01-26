from django.db import models
 
# Creación de campos de la tabla 'postres' 
class Productos(models.Model):
    nombre = models.CharField(max_length=100, default='')
    precio = models.CharField(max_length=20, default='0.0')
    stock = models.CharField(max_length=100, default='0')

    class Meta:
         db_table = 'productos' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos
 
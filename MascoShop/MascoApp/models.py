from django.db import models

# Create your models here.

class Categoria (models.Model): 
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    producto = models.CharField(max_length=20, primary_key=True, verbose_name='Producto')
    marca= models.CharField(max_length=20, verbose_name='Marca')
    nombre=models.CharField(max_length=30, verbose_name='Nombre')
    descripcion=models.CharField(max_length=40, verbose_name='Descripcion')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="producto",null=True)

    def __str__(self):
        return self.producto

class Cliente(models.Model):
    run = models.CharField(max_length=9, primary_key=True, verbose_name='Run')
    genero= models.CharField(max_length=12, verbose_name='Genero')
    nombrecliente=models.CharField(max_length=40, verbose_name='NombreCliente')
    edad=models.IntegerField(verbose_name='Edad')
    estado=models.CharField(max_length=12, verbose_name='Estado')
    ocupacion=models.CharField(max_length=40, verbose_name='Ocupacion')

    def __str__(self):
        return self.run
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria
from .models import Producto
from .models import Cliente


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['producto', 'marca', 'nombre', 'descripcion', 'categoria']
        labels ={
            'producto': 'Producto', 
            'marca': 'Marca', 
            'nombre': 'Nombre', 
            'descripcion': 'Descripcion',
            'categoria' : 'Categoria',
        }
        widgets={
            'producto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id del producto', 
                    'id': 'producto'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca del producto', 
                    'id': 'marca'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del producto', 
                    'id': 'nombre'
                }
            ), 
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese descripcion del producto', 
                    'id': 'descripcion'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['run', 'genero', 'nombrecliente', 'edad', 'estado','ocupacion']
        labels ={
            'run': 'Run', 
            'genero': 'Genero', 
            'nombrecliente': 'NombreCliente', 
            'edad': 'Edad',
            'estado' : 'Estado',
            'ocupacion' : 'Ocupacion',
        }
        widgets={
            'run': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su run', 
                    'id': 'run'
                }
            ), 
            'genero': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su genero', 
                    'id': 'genero'
                }
            ), 
            'nombrecliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombrecliente'
                }
            ), 
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su edad', 
                    'id': 'edad'
                }
            ), 
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su estado civil', 
                    'id': 'estado',
                }
            ), 
            'ocupacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su ocupacion', 
                    'id': 'ocupacion',
                }
            )
            

        }

 
    
     


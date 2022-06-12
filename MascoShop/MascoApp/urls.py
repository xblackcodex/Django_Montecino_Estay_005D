from unicodedata import name
from django.urls import path 
from .views import form_del_producto, form_producto, home,somos,registrar,galeria,feriados,form_modproducto,form_del_producto,mostrar,ejemplo,mostrar_cliente,form_del_cliente,form_cliente,form_modcliente,form_del_cliente

urlpatterns = [ 
    path('',home,name="home"),
    path('somos/',somos,name="somos"),
    path('registrar/',registrar,name="registrar"),
    path('galeria/',galeria,name="galeria"),
    path('mostrar/',mostrar, name="mostrar"),
    path('feriados/',feriados,name="feriados"),
    path('form_producto/',form_producto,name="form_producto"),
    path('form_modproducto/<id>',form_modproducto,name="form_modproducto"),
    path('form_del_producto/<id>',form_del_producto,name="form_del_producto"),
    path('ejemplo/',ejemplo,name="ejemplo"),
    path('mostrar_cliente/',mostrar_cliente,name="mostrar_cliente"),
    path('form_del_cliente/<id>',form_del_cliente,name="form_del_cliente"),
    path('form_cliente/',form_cliente,name="form_cliente"),
    path('form_modcliente/<id>',form_modcliente,name="form_modcliente"),
] 
from django.urls import path

from . import views
from .views import exit, register

#app_name = "paneldecontrol"
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home_view, name="home"),
    path("register/", register, name="register"),
    path("registros/", views.registros, name="registros"),
    path("registroproducto/", views.registroproducto, name="registroproducto"),
    path("inventario/", views.inventario, name="inventario"),
    path("registrar-produ/", views.añadir, name="añadir"),
    path("contact/", views.contact_view, name="contact"),
    path("logout/", exit, name='exit'),
    path("editarprodu/<codigo>", views.editarprodu),
    path("edicionprodu/<codigo>", views.edicionprodu, name="edicion"),
    path("borrarproducto/<codigo>", views.borrarprodu, name="borrar"),
]
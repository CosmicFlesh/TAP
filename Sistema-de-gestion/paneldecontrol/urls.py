from django.urls import path

from . import views
from .views import exit, register

#app_name = "paneldecontrol"
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home_view, name="home"),
    path("register/", register, name="register"),
    path("registros/", views.registros, name="registros"),
    path("inventario/", views.inventario, name="inventario"),
    path("registar-produ/", views.añadir, name="añadir"),
    path("contact/", views.contact_view, name="contact"),
    path("logout/", exit, name='exit')

]
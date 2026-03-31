import datetime
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    usuario_text = models.CharField(max_length=200)
   # contraseña = models.ForeignKey(Contraseña, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.usuario_text


class Contraseña(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contraseña_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
    def __str__(self):
        return self.contraseña_text
    
class Marca(models.Model):
    
    marca = models.CharField(max_length=120)
    def __str__(self):
        return self.marca

class Categoria(models.Model):
    categoria = models.CharField(max_length=120)
    def __str__(self):
        return self.categoria
   
class Inventario(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6, default=1)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombreproducto = models.CharField(max_length=350)
    cantidad = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.nombreproducto
# Create your models here.

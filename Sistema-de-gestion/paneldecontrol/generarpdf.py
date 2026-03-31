from django.template.loader import get_template
from .models import Inventario

def pdfinador():
    template = get_template("modelopdf.html")
    context = {"codigo":Inventario.codigo,
               "usuario":Inventario.usuario,
               "nombreprodu":Inventario.nombreproducto,
               "cantidad":Inventario.cantidad,
               "categoria":Inventario.categoria,
               "marca":Inventario.marca,
               "fecha":Inventario.pub_date,                           
               }
    html_template = template.render(context)
    

pdfinador()
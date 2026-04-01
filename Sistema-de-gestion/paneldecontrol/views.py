from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.template.loader import render_to_string
from .form import ContactForm
from .form import CustomUserCreationForm
from .form import SubmitProduct
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Usuario
from .models import Inventario
from .models import Categoria
from .models import Marca

def index(request):
    return render(request, "paneldecontrol/index.html")

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
    return render(request, 'registration/register.html', data)

def añadirproducto(request):
    if request.method == 'POST':
        form = SubmitProduct(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('success_page')
    else:
        form = SubmitProduct()
    return render(request, 'paneldecontrol/inventario.html', {'form': form})

def registroproducto(request):
     if request.method == 'POST':
        # 1. Obtener datos del formulario
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        categoria_id = request.POST['categoria'] # Recibimos el ID del select
        marca_id = request.POST['marca']       # Recibimos el ID del select

        # 2. Crear el objeto (usando _id para las ForeignKey)
        Inventario.objects.create(
            nombreproducto=nombre, 
            cantidad=cantidad, 
            categoria_id=categoria_id, # Django acepta el ID directamente con _id
            marca_id=marca_id
        )
        return redirect('inventario')
    # Si es GET, cargamos las opciones para los selects
     categorias = Categoria.objects.all()
     marcas = Marca.objects.all()
     return render(request, 'paneldecontrol/añadir.html', {
        'categorias': categorias,
        'marcas': marcas
    })
  
def exportar_pdf(request):
    # 1. Obtener los datos
    registros = Inventario.objects.all()
    # 2. Renderizar el template HTML a una cadena (string)
    context = {'registros': registros}
    html_string = render_to_string('reportes/modelopdf.html', context)
    # 3. Crear el objeto de respuesta PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_registros.pdf"'
    # 4. Generar el PDF
    # HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(response)
    
    return response

def editarprodu(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    cantidad = request.POST['txtcantidad']
    categoria_id = request.POST['txtcategoria'] 
    marca_id = request.POST['txtmarca'] 

    producto = Inventario.objects.get(codigo=codigo)
    producto.nombreprodu = nombre
    producto.cantidad = cantidad
    producto.categoria = categoria_id
    producto.marca = marca_id
    producto.save()
    
    return redirect('inventario')

def edicionprodu(request, codigo):
    producto = Inventario.objects.get(codigo=codigo)
    return render(request, "paneldecontrol/edicionprodu.html", {"Inventario": producto})

def borrarprodu(request, codigo):
    producto = Inventario.objects.get(codigo=codigo)
    producto.delete()
    return redirect('inventario')


def exit(request):
    logout(request)
    return redirect('index')

@login_required
def registros(request):
    return render(request, "paneldecontrol/registros.html")

@login_required
def añadir(request):
    return render(request, "paneldecontrol/añadir.html")

@login_required
def inventario(request):
    productos = Inventario.objects.all()
    context = {'rows': productos}
    return render(request, 'paneldecontrol/inventario.html', context)

# pagina para la funcion home_view
def home_view(request):
    return render(request, 'paneldecontrol/home.html')

# define la funcion contact_view para handlear el form de contacto
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.enviar_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
        context = {'form': form}
        return render(request, 'paneldecontrol/contact.html', context)

# define la funcion contact_success_view para handlear el success
def contact_success_view(request):
    return render(request, 'paneldecontrol/contact_success.html')

# Create your views here.

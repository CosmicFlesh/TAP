from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.template import loader
from django.http import Http404
from .form import ContactForm
from .form import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Usuario
from .models import Inventario


def index(request):
    try:
        latest_usuario_list = Usuario.objects.order_by("-pub_date")[:5]
        context = {"latest_usuario_list": latest_usuario_list}
    except Usuario.DoesNotExist:
        raise Http404("No hay nada")
    return render(request, "paneldecontrol/index.html", context)

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
    try:
        invent =Inventario.objects.order_by("-pub_date")[:5]
        context = {"invent" : invent}
    except Inventario.DoesNotExist:
        raise Http404("no hay inventario")
    return render(request, "paneldecontrol/inventario.html", context)
    
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

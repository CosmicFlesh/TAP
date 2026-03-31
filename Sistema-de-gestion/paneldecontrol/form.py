from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Inventario
from .models import Usuario
from .models import Categoria
from .models import Marca
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SubmitProduct(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['codigo','usuario', 'nombreproducto', 'cantidad', 'categoria', 'marca','pub_date']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    contraseña = forms.PasswordInput()
    mensage = forms.CharField(widget=forms.Textarea)

    def enviar_email(self):
        print(f"enviando email de {self.cleaned_data['email']} con mensaje: {self.cleaned_data ['mensage']}")
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
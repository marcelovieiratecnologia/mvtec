from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['nome', 'email', 'assunto', 'mensagem'] # ao invés de eu chamar um por um colocar __all__ que economiza digitação
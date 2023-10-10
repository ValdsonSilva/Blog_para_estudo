from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','telefone','email','mensagem']
       
    
    nome = forms.CharField(
        label = 'Nome:',
        widget = forms.TextInput(attrs={'class':'entrada', 'placeholder':'nome'}),
    )
    
    telefone = forms.CharField(
        label = 'Telefone:',
        widget = forms.TextInput(attrs={'class':'entrada','placeholder':'telefone'}),
    )
    
    email = forms.EmailField(
        label = 'Email:',
        widget = forms.TextInput(attrs={'class':'entrada', 'placeholder':'email'}),
    )
    
    mensagem = forms.CharField(
        label = 'Mensagem:',
        widget = forms.TextInput(attrs={'class':'entrada', 'placeholder':'mensagem'}),
    )
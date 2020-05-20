from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
import re
from django.forms.widgets import ClearableFileInput
from carona.models import Custom_user
from carona.models import Carona
from carona.models import Carro



class UsuarioModelForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['email', 'password', 'first_name', 'username']

class CustomUserModelForm(forms.ModelForm):
	imagem_cad = forms.ImageField(widget = ClearableFileInput)

	class Meta:
		model = Custom_user
		fields = ['imagem_cad']

class CaronaModelForm(forms.ModelForm):
	
	class Meta:
		model = Carona
		fields = ['origem', 'destino', 'data', 'num_passageiros', 'preco', 'hora_saida', 'hora_chegada']

class CarroModelForm(forms.ModelForm):
	imagem_carro = forms.ImageField(widget = ClearableFileInput)
	
	class Meta:
		model = Carro
		fields = ['modelo', 'ano', 'imagem_carro']
		

class ConsultCaronaModelForm(forms.ModelForm):

	class Meta:
		model = Carona
		fields = ['origem', 'destino', 'data']

class PerfilModelForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ['email', 'first_name', 'username']
		widgets = {
			'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'* Email Exemplo@gmail.com..'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'* Nome..'}),
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'* Nome de Usuario...'}),
		}
		
	
		
		
		


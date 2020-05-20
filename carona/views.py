from django.shortcuts import render
from django.shortcuts import render, redirect
from carona.models import User
from carona.models import Carona
from carona.models import Custom_user
from carona.models import Carro
from carona.forms import CaronaModelForm
from carona.forms import CarroModelForm
from carona.forms import UsuarioModelForm
from carona.forms import CustomUserModelForm
from carona.forms import ConsultCaronaModelForm
from carona.forms import PerfilModelForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout, authenticate



def getCustonUser(request):
	custon_user = None
	if request.user.is_authenticated and request.user.is_superuser == False:
		custon_user = Custom_user.objects.get(user_id = request.user.id)
		return custon_user
	else:
		return custon_user

def index(request):
	custon_user = getCustonUser(request)
	return render(request, 'index.html', {'custon_user':custon_user})


def procurar(request):
	custon_user = getCustonUser(request)
	return render(request, 'procurar.html', {'custon_user':custon_user})


def ofertarCarona(request):
	custon_user = getCustonUser(request)
	if request.method == 'POST':
		form = CaronaModelForm(request.POST)
		if form.is_valid():
			origem = form.cleaned_data.get('origem')
			destino = form.cleaned_data.get('destino')
			data = form.cleaned_data.get('data')
			num_passageiros = form.cleaned_data.get('num_passageiros')
			preco = form.cleaned_data.get('preco')
			hora_saida = form.cleaned_data.get('hora_saida')
			hora_chegada = form.cleaned_data.get('hora_chegada')
			carona = Carona.objects.create(origem=origem, destino=destino, data=data, num_passageiros=num_passageiros, preco=preco, hora_saida=hora_saida, hora_chegada=hora_chegada, usuario_id = custon_user.id)
			return redirect('/detalhesCarona/', {'carona':carona, 'custon_user':custon_user})
		
	else:
		return render(request, 'ofertarCarona.html', {'custon_user':custon_user})


def cadastro(request):
	custon_user = getCustonUser(request)
	return render(request, 'cadastro.html', {'custon_user':custon_user})

def submit_login(request):
	custon_user = getCustonUser(request)
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('/')
	else:
		return render(request, 'login.html', {'custon_user':custon_user})


def perfil(request):
	form = PerfilModelForm(instance = request.user)
	custon_user = getCustonUser(request)
	return render(request, 'perfil.html', {'custon_user':custon_user, 'form':form})

def submit_con_carona(request):
	form = ConsultCaronaModelForm(request.POST)
	custon_user = getCustonUser(request)
	if request.method == 'POST':
		if form.is_valid():
			origem = form.cleaned_data.get('origem')
			destino = form.cleaned_data.get('destino')
			data = form.cleaned_data.get('data')
			caronas = Carona.objects.filter(origem = origem, destino = destino, data = data).select_related()
			print(caronas)
			return render(request, 'caronasEncontradas.html', {'caronas':caronas, 'custon_user':custon_user})
		else:
			return redirect('/procurar/')
	else:
		return redirect('/procurar/')

def detalhesCarona(request, idi):
	custon_user = getCustonUser(request)
	carona = Carona.objects.get(id_carona = idi)
	return render(request, 'detalhesCarona.html', {'custon_user':custon_user, 'carona':carona})

def submit_cadastro(request):
	form = UsuarioModelForm(request.POST)
	form2 = CustomUserModelForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid() and form2.is_valid():
			email = form.cleaned_data.get('email')
			first_name = form.cleaned_data.get('first_name')
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			new_user = User.objects.create_user(username, email, password, first_name=first_name)
			imagem_cad = form2.cleaned_data.get('imagem_cad')
			user_custon = Custom_user.objects.create(user = new_user, imagem_cad = imagem_cad)
			return redirect('/login/')
		else:
			return redirect('/cadastro/')

	else:
		redirect('/cadastro/')

def alteraFoto(request, id_user):
	if request.method == 'POST':
		custon_user = Custom_user.objects.get(user_id = id_user)
		form = PerfilModelForm(instance = request.user)
		form2 = CustomUserModelForm(request.POST, request.FILES, instance = custon_user)
		custon_user = getCustonUser(request)
		if form2.is_valid():
			form2.save()
			return redirect('/perfil/')
	return render(request, 'perfil.html', {'custon_user':custon_user, 'form':form, 'form2':form2})

def alteraDadosUsuario(request, id_usuario):
	if request.method == 'POST':
		custon_user = Custom_user.objects.get(user_id = id_usuario)
		form2 = CustomUserModelForm(request.POST, request.FILES, instance = custon_user)
		form = PerfilModelForm(request.POST, instance = request.user)
		if form.is_valid():
			print("sss")
			form.save()
			return redirect('/perfil/')
		else:
			return render(request, 'perfil.html', {'custon_user':custon_user, 'form':form, 'form2':form2})
	return redirect('/perfil/')


def alterarSenha(request):
	custon_user = getCustonUser(request)
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user) 
			messages.success(request, 'Your password was successfully updated!')
			render(request, 'alterarSenha.html', {'form':form, 'custon_user':custon_user})
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user, request.POST)
	return render(request, 'alterarSenha.html', {'form':form, 'custon_user':custon_user})

def cadastroCarro(request):
	custon_user = getCustonUser(request)
	form = CarroModelForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			modelo = form.cleaned_data.get('modelo')
			ano = form.cleaned_data.get('ano')
			imagem_carro = form.cleaned_data.get('imagem_carro')
			new_carro = Carro.objects.create(modelo = modelo, ano = ano, imagem_carro = imagem_carro, id_usuario_id = request.user.id)
			return render(request, 'cadastroCarro.html', {'custon_user':custon_user})
	else:
		return render(request, 'cadastroCarro.html', {'custon_user':custon_user})

def perfilPublico(request, user_id):
	custon_user = getCustonUser(request)
	user = Custom_user.objects.select_related('user').get(user_id = user_id)
	return render(request, 'perfilPublico.html', {'custon_user':custon_user, 'usuario':user})

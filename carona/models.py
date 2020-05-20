from django.db import models
from django.contrib.auth.models import User


class Custom_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem_cad = models.ImageField(upload_to='media/%Y/%m/%d/', null=True, blank=True)
    telefone = models.TextField(max_length = 20)


class Carona(models.Model):
	id_carona = models.IntegerField(primary_key=True)
	origem = models.TextField(max_length = 100)
	destino = models.TextField(max_length = 100)
	data = models.DateField()
	num_passageiros = models.IntegerField()
	preco = models.FloatField()
	hora_saida = models.TimeField()
	hora_chegada = models.TimeField()
	usuario = models.ForeignKey(Custom_user, on_delete = models.CASCADE)

class Carro(models.Model):
	modelo = models.TextField(max_length = 100)
	ano = models.IntegerField()
	imagem_carro = models.ImageField(upload_to='media2/%Y/%m/%d/', null=True, blank=True)
	id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)

class Passageiros(models.Model):
	id_pasageiro = models.ForeignKey(User, on_delete = models.CASCADE)
	id_carona = models.ForeignKey(Carona, on_delete = models.CASCADE)

		


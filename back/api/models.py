from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)



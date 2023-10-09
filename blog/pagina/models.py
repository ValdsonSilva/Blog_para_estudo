from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    mensagem = models.TextField()
    
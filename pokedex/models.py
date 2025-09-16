from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=100, unique=True)
    imagem = models.URLField(unique=True)

    def __str__(self):
        return self.nome
    

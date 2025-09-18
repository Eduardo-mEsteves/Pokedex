
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    pokemon_id = models.PositiveIntegerField(unique=True)
    nome       = models.CharField(max_length=250, verbose_name="Nome do pokemon:")
    img        = models.URLField()
    peso       = models.FloatField()
    tipo1      = models.CharField(max_length=20)
    tipo2      = models.CharField(max_length=20, blank=True)
    hp         = models.IntegerField()
    forca      = models.IntegerField()
    defesa     = models.IntegerField()
    forca_esp  = models.IntegerField()
    defesa_esp = models.IntegerField()
    velocidade = models.IntegerField()

    class Meta:
        verbose_name = "Pokemon Favorito"
        verbose_name_plural = "Pokemons Favoritos"

    # Como ele vai aparecer lá no django Admin
    def __str__(self):
        return f"{self.nome} #{self.pokemon_id}"

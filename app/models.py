from django.db import models

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    ano = models.IntegerField()
    def __str__(self):
        return self.modelo

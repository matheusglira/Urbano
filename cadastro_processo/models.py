from django.db import models

# Create your models here.
class Planilha(models.Model):
    nome = models.TextField()
    cliente = models.TextField()
    arquivo = models.FileField()
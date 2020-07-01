from django.db import models

# Create your models here.

class Processo(models.Model):
    pasta = models.TextField()
    comarca = models.TextField()
    uf = models.TextField()
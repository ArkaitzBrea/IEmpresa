from django.db import models


class Cliente(models.Model):
    cif = models.CharField(max_length=12, primary_key=True)
    nombre_empresa = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField(max_length=9, unique=True)
    nombre_cliente = models.CharField(max_length=20)

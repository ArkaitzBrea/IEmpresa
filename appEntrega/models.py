from django.db import models


# Tabla cliente
class Cliente(models.Model):
    cif = models.CharField(max_length=12, primary_key=True)
    nombre_empresa = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField(max_length=9, unique=True)
    nombre_cliente = models.CharField(max_length=20)


class Pedido(models.Model):
    pedido_referencia = models.CharField(max_length=12, primary_key=True)
    pedido_fecha = models.DateField()
    pedido_precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pedido_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Producto(models.Model):
    producto_referencia = models.CharField(max_length=12, primary_key=True)
    producto_nombre = models.CharField(max_length=50)
    producto_descripcion = models.CharField(max_length=250)
    producto_categoria = models.CharField(max_length=50)


class Componente(models.Model):
    producto_referencia_padre = models.ForeignKey(Producto, on_delete=models.CASCADE)
    producto_referencia = models.ForeignKey(Producto, on_delete=models.CASCADE)
    componente_cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    componente_descripcion = models.CharField(max_length=250);

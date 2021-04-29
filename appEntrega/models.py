from django.db import models


# Tabla cliente
class Cliente(models.Model):
    cif = models.CharField(max_length=12, primary_key=True)
    nombre_empresa = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField(unique=True)
    nombre_cliente = models.CharField(max_length=20)

    # Funcion que devuelve el nombre_empresa cuando se visualiza en el /admin
    def __str__(self):
        return self.nombre_empresa


class Producto(models.Model):
    producto_referencia = models.CharField(max_length=13, primary_key=True)                     
    producto_nombre = models.CharField(max_length=50)   
    producto_descripcion = models.CharField(max_length=250) 
    producto_categoria = models.CharField(max_length=50)    
    producto_precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Funcion que devuelve el producto_nombre cuando se visualiza en el /admin
    def __str__(self):
        return self.producto_nombre


class Componente(models.Model):
    componente_producto_padre = models.ForeignKey(Producto, related_name='producto_padre', null=False,
                                                  on_delete=models.CASCADE,
                                                  default=0)
    componente_producto = models.ForeignKey(Producto, related_name='producto', null=False, on_delete=models.CASCADE,
                                            default=0)
    componente_unidades = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    componente_descripcion = models.CharField(max_length=250)

    # Funcion que devuelve el producto cuando se visualiza en el /admin
    def __str__(self):
        return str(self.producto)   


class Orden_Pedido(models.Model):
    pedido_referencia = models.CharField(max_length=12, primary_key=True)   
    pedido_fecha = models.DateField(auto_now=True)
    pedido_descripcion = models.TextField(max_length=250)
    cantidad = models.PositiveIntegerField()
    pedido_cliente_cif = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    # CREO QUE FALTA OTRA FOREIGNKEY


class Factura(models.Model):
    linea_referencia = models.CharField(max_length=12, primary_key=True)
    linea_descripcion = models.CharField(max_length=250)
    linea_unidades = models.PositiveIntegerField()
    linea_precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    linea_pedido_referencia = models.ForeignKey(Orden_Pedido, on_delete=models.CASCADE)
    linea_producto_referencia = models.ForeignKey(Producto, on_delete=models.CASCADE)
    linea_linea_padre = models.ForeignKey('self', on_delete=models.CASCADE)

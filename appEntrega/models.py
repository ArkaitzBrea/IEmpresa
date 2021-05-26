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


# Tabla producto
class Producto(models.Model):
    producto_referencia = models.CharField(max_length=13, primary_key=True)
    producto_nombre = models.CharField(max_length=50)
    producto_descripcion = models.CharField(max_length=250)
    producto_categoria = models.CharField(max_length=50)
    producto_precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #Atributo fichero
    producto_pdf = models.FileField(blank=True,null=True)

    # Funcion que devuelve el producto_nombre cuando se visualiza en el /admin
    def __str__(self):
        return self.producto_nombre


# Tabla componente
class Componente(models.Model):
    componente_producto_padre = models.ForeignKey(Producto, related_name='producto_padre', null=False,
                                                  on_delete=models.CASCADE,
                                                  default=0)
    componente_producto = models.ForeignKey(Producto, related_name='producto', null=False, on_delete=models.CASCADE,
                                            default=0)
    componente_unidades = models.PositiveIntegerField(default=1)
    componente_descripcion = models.CharField(max_length=250)

    # Funcion que devuelve el producto cuando se visualiza en el /admin
    def __int__(self):
        return self.componente_descripcion


# Tabla orden_pedido
class Orden_Pedido(models.Model):
    pedido_referencia = models.CharField(max_length=12, primary_key=True)
    pedido_fecha = models.DateField(auto_now=True)
    pedido_descripcion = models.TextField(max_length=250)
    pedido_cliente_cif = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    # Funcion que devuelve la orden de pedido cuando se visualiza en el /admin
    def __int__(self):
        return self.pedido_descripcion

    def __str__(self):
        return self.pedido_descripcion


# Tabla factura
class Factura(models.Model):
    referencia = models.CharField(max_length=12, primary_key=True)
    pedido_referencia = models.ForeignKey(Orden_Pedido, on_delete=models.CASCADE)
    producto_referencia = models.ForeignKey(Producto, on_delete=models.CASCADE)
    unidades = models.PositiveIntegerField(default=1)
    linea_precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descripcion = models.TextField(max_length=250)

    # Funcion que devuelve la factura cuando se visualiza en el /admin
    def __int__(self):
        return self.descripcion

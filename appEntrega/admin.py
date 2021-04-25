from django.contrib import admin
from .models import Cliente, Producto, Componente, Orden_Pedido, Orden_Linea

# Aquí se registran los modelos/tablas
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(Orden_Pedido)
admin.site.register(Orden_Linea)

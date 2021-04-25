from django.contrib import admin
from  .models import Cliente, Producto, Componente, Pedido

# Aquí se registran los modelos/tablas
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(Pedido)


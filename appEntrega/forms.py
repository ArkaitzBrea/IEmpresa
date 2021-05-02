from django import forms
from .models import Producto, Cliente, Componente, Orden_Pedido, Factura


# Formulario nuevo producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


# Formulario nuevo cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


# Formulario nuevo componente
class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'


# Formulario nuevo pedido
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Orden_Pedido
        fields = '__all__'


# Formulario nueva  factura
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'

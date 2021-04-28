from django import forms
from .models import Producto, Cliente, Componente,Orden_Pedido


#Formulario nuevo producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

#Formulario nuevo cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

#Formulario nuevo cliente
class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'

#Formulario nuevo cliente
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Orden_Pedido
        fields = '__all__'
from django import forms
from .models import Producto, Cliente, Componente, Orden_Pedido, Factura


# Formulario nuevo producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    producto_referencia = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'formulario__input'}))
    producto_nombre = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'formulario__input'}))
    producto_descripcion = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'formulario__input'}))
    producto_categoria = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'formulario__input'}))
    producto_precio = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class': 'formulario__input'}))

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
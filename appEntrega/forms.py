from django import forms
from .models import Producto


#Formulario nuevo producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

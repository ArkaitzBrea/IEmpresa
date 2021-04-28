from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .models import Orden_Pedido
from .forms import ProductoForm





# Vista de PedidoListView
class PedidoListView(ListView):
    model = Orden_Pedido
    # queryset = Empleado.objects.all()
    template_name = 'listaPedidos.html'
    context_object_name = 'lista_pedidos'


# Vista de PedidoDetailView
class PedidoDetailView(DetailView):
    model = Orden_Pedido
    # queryset = Empleado.objects.all()
    template_name = 'detallePedido.html'
    context_object_name = 'pedido'


class CreateProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear producto'
        }
        return render(request, 'nuevoProducto.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()

            # Volvemos a la lista de noticias
            return redirect('producto_form')

        return render(request, 'nuevoProducto.html', {'form': form})


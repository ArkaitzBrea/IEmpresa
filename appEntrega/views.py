from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Orden_Pedido


# Vista Index
def index(request):
    return HttpResponse("Hola Amigos!!")


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

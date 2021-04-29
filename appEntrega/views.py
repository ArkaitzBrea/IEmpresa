from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView
from django.views import View
from .models import Orden_Pedido, Cliente, Producto
from .forms import ProductoForm, ClienteForm, ComponenteForm, PedidoForm
from django.urls import reverse_lazy

# Vista de PedidoListView
class PedidoListView(ListView):
    model = Orden_Pedido
    template_name = 'listaPedidos.html'
    context_object_name = 'lista_pedidos'

# Vista de PedidoDetailView
class PedidoDetailView(DetailView):
    model = Orden_Pedido
    template_name = 'detallePedido.html'
    context_object_name = 'pedido'

# Vista de ClienteListView
class ClienteListView(ListView):
    model = Cliente
    template_name = 'listaClientes.html'
    context_object_name = 'lista_clientes'


# Vista de ClienteDetailView
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'detalleCliente.html'
    context_object_name = 'cliente'

# Vista de ProductoListView
class ProductoListView(ListView):
    model = Producto
    template_name = 'listaProductos.html'
    context_object_name = 'lista_productos'

# Vista de ProductoDetailView
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'detalleProducto.html'
    context_object_name = 'producto'

# Vista de formulario de crear un nuevo producto
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

            # Volvemos a la pagina que queramos despues de crear un nuevo producto
            return redirect("listaProducto")

        return render(request, 'nuevoProducto.html', {'form': form})


# Vista de formulario de crear un nuevo cliente
class CreateClienteView(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear cliente'
        }
        return render(request, 'nuevoCliente.html', context)

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()

            # Volvemos a la pagina que queramos despues de crear un nuevo producto
            return redirect("listaCliente")

        return render(request, 'nuevoCliente.html', {'form': form})


# Vista de formulario de crear un nuevo componente
class CreateComponenteView(View):
    def get(self, request, *args, **kwargs):
        form = ComponenteForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear componente'
        }
        return render(request, 'nuevoComponente.html', context)

    def post(self, request, *args, **kwargs):
        form = ComponenteForm(request.POST)
        if form.is_valid():
            form.save()

            # Volvemos a la pagina que queramos despues de crear un nuevo producto
            return redirect("listaComponente")

        return render(request, 'nuevoComponente.html', {'form': form})


# Vista de formulario de crear un nuevo pedido
class CreatePedidoView(View):
    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Nuevo pedido'
        }
        return render(request, 'nuevoPedido.html', context)

    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()

            # Volvemos a la pagina que queramos despues de crear un nuevo producto
            return redirect("listaPedido")

        return render(request, 'nuevoPedido.html', {'form': form})

class DeleteProductoView(DeleteView):
    model = Producto
    template_name ='borrar.html'
    success_url = reverse_lazy('listaProducto')

class DeletePedidoView(DeleteView):
    model = Orden_Pedido
    template_name ='borrar.html'
    success_url = reverse_lazy('listaPedido')

class DeleteClienteView(DeleteView):
    model = Cliente
    template_name ='borrar.html'
    success_url = reverse_lazy('listaCliente')

class UpdateClienteView(UpdateView):
    model = Cliente
    template_name = 'update.html'
    fields = ['email','telefono','nombre_cliente']
    success_url = reverse_lazy('listaCliente')

class UpdateProductoView(UpdateView):
    model = Producto
    template_name = 'update.html'
    fields = ['producto_nombre','producto_descripcion','producto_categoria','producto_precio']
    success_url = reverse_lazy('listaProducto')

class UpdatePedidoView(UpdateView):
    model = Orden_Pedido
    template_name = 'update.html'
    fields = ['pedido_descripcion','cantidad']
    success_url = reverse_lazy('listaPedido') 
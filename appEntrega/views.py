from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.views import View
from .models import Orden_Pedido, Cliente, Producto, Componente, Factura
from .forms import ProductoForm, ClienteForm, ComponenteForm, PedidoForm, FacturaForm
from django.urls import reverse_lazy


# Index
def Index(request):
    context = {'foo': 'bar'}
    return render(request, 'index.html', context)


# clasas de LISTA
# Vista de PedidoListView
class PedidoListView(ListView):
    model = Orden_Pedido
    template_name = 'listaPedidos.html'
    context_object_name = 'lista_pedidos'


# Vista de ClienteListView
class ClienteListView(ListView):
    model = Cliente
    template_name = 'listaClientes.html'
    context_object_name = 'lista_clientes'


# Vista de ProductoListView
class ProductoListView(ListView):
    model = Producto
    template_name = 'listaProductos.html'
    context_object_name = 'lista_productos'


# Vista de FacturaListView
class FacturaListView(ListView):
    model = Factura
    template_name = 'listaFacturas.html'
    context_object_name = 'lista_facturas'


# Clases de DETAIL
# Vista de ClienteDetailView
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'detalleCliente.html'
    context_object_name = 'cliente'


# Vista de PedidoDetailView
class PedidoDetailView(DetailView):
    model = Orden_Pedido
    template_name = 'updatePedido.html'
    context_object_name = 'pedido'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_facturas'] = Factura.objects.all().filter(pedido_referencia=self.kwargs['pk'])
        return context
    
    
    # Editar Pedido
    class UpdatePedidoView(UpdateView):
        model = Orden_Pedido
        # template_name = 'updatePedido.html'
        fields = ['pedido_descripcion', 'pedido_referencia', 'pedido_cliente_cif']
        success_url = reverse_lazy('listaPedido')


# Vista de FacturaDetailView
class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'detalleFactura.html'
    context_object_name = 'factura'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_productos'] = Producto.objects.all().filter(producto_referencia=self.kwargs['pk'])
        return context

    # Editar Factura
    class UpdateFacturaView(UpdateView):
        model = Factura
        #template_name = 'updateFactura.html'
        fields = ['pedido_referencia', 'producto_referencia', 'unidades', 'descripcion']
        success_url = reverse_lazy('listaPedido')


# Vistas para AÑADIR/CREAR
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


# Vista de formulario de crear una nueva factura
class CreateFacturaView(View):
    def get(self, request, *args, **kwargs):
        form = FacturaForm()
        context = {
            'form': form,
            'titulo_pagina': 'Nueva factura'
        }
        return render(request, 'nuevoFactura.html', context)

    def post(self, request, *args, **kwargs):
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()

            # Volvemos a la pagina que queramos despues de crear un nuevo producto
            return redirect("listaPedidos")

        return render(request, 'nuevoFactura.html', {'form': form})


# Clases para eliminar
# Borrar Producto
class DeleteProductoView(DeleteView):
    model = Producto  # modelo en el que se basa
    template_name = 'borrarProducto.html'  # html que utiliza
    success_url = reverse_lazy('listaProducto')  # si la eliminacion es correcta cual es su siguiente direccion


# Borrar Pedido
class DeletePedidoView(DeleteView):
    model = Orden_Pedido
    template_name = 'borrarPedido.html'
    success_url = reverse_lazy('listaPedido')


# Borrar Cliente
class DeleteClienteView(DeleteView):
    model = Cliente
    template_name = 'borrarCliente.html'
    success_url = reverse_lazy('listaCliente')


# Borrar Factura
class DeleteFacturaView(DeleteView):
    model = Factura
    template_name = 'borrar.html'
    success_url = reverse_lazy('listaProducto')


# Borrar Componente
class DeleteComponenteView(DeleteView):
    model = Componente
    template_name = 'borrarComponente.html'
    success_url = reverse_lazy('listaProducto')


# Clases para editar
# Editar Cliente
class UpdateClienteView(UpdateView):
    model = Cliente  # model en el que se basa
    template_name = 'update.html'  # html que utiliza
    fields = ['email', 'telefono', 'nombre_cliente']  # campos editables
    success_url = reverse_lazy('listaCliente')  # URL a la que redirecciona


class ProductoDetailView(DetailView):
    model = Producto
    #template_name = 'detalleProducto.html'
    context_object_name = 'producto'
    template_name = 'updateProducto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_componentes'] = Componente.objects.all().filter(componente_producto_padre=self.kwargs['pk'])
        return context

    class UpdateProductoView(UpdateView):
        model = Producto
        #template_name = 'updateProducto.html'
        fields = ['producto_nombre', 'producto_descripcion', 'producto_categoria', 'producto_precio']
        success_url = reverse_lazy('listaProducto')

# Editar Componente
class UpdateComponenteView(UpdateView):
    model = Componente
    template_name = 'update.html'
    fields = ['componente_producto_padre', 'componente_producto', 'componente_unidades', 'componente_descripcion']
    success_url = reverse_lazy('listaPedido')

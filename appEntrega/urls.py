from django.urls import path
from . import views
<<<<<<< HEAD
from appEntrega.views import PedidoDetailView, PedidoListView,CreateProductoView,CreateClienteView,CreateComponenteView, CreatePedidoView, ClienteDetailView, ClienteListView, ProductoListView, ProductoDetailView, DeleteProductoView,DeletePedidoView,DeleteClienteView,UpdateClienteView,UpdateProductoView,UpdatePedidoView

urlpatterns = [
    # URL detalle pedido
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='detallePedido'),
=======
from appEntrega.views import PedidoDetailView, PedidoListView, CreateProductoView, CreateClienteView, \
    CreateComponenteView, CreatePedidoView, ClienteDetailView, ClienteListView, ProductoListView, ProductoDetailView, \
    DeleteProductoView, DeletePedidoView, DeleteClienteView, Index,UpdateClienteView,UpdatePedidoView,UpdateProductoView

urlpatterns = [
    # URL detalle pedido
    path('', Index, name='index'),
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='detallePedido'),
>>>>>>> 2c3aeff862fb84e121d835ec1bfa63948475056b
    # URL lista pedidos
    path('pedidos/', PedidoListView.as_view(), name='listaPedido'),
    # URL detalle cliente
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name='detalleCliente'),
    # URL lista clientes
    path('clientes/', ClienteListView.as_view(), name='listaCliente'),
    # URL detalle producto
    path('productos/<str:pk>', ProductoDetailView.as_view(), name='detalleProducto'),
    # URL lista productos
    path('productos/', ProductoListView.as_view(), name='listaProducto'),
    # URL nuevo producto
    path('productos/nuevo/', views.CreateProductoView.as_view(), name='producto_form'),
    # URL nuevo cliente
    path('clientes/nuevo/', views.CreateClienteView.as_view(), name='cliente_form'),
    # URL nuevo componente
    path('componentes/nuevo/', views.CreateComponenteView.as_view(), name='componente_form'),
    # URL nuevo orden_pedido
    path('pedidos/nuevo/', views.CreatePedidoView.as_view(), name='pedido_form'),
<<<<<<< HEAD
    #URL borrar producto
    path('productos/<int:pk>/delete/', DeleteProductoView.as_view(),name='borrar_producto'),
    #URL borrar cliente
    path('clientes/<int:pk>/delete/', DeleteClienteView.as_view(),name='borrar_clientes'),
    #URL borrar pedido
    path('pedidos/<int:pk>/delete/', DeletePedidoView.as_view(),name='borrar_pedidos'),
    #URL editar cliente
    path('clientes/<pk>/editar', UpdateClienteView.as_view(),name='editar_cliente'),
    #URL editar cliente
    path('productos/<pk>/editar/', UpdateProductoView.as_view(),name='editar_cliente'),
    #URL editar cliente
    path('pedidos/<pk>/editar/', UpdatePedidoView.as_view(),name='editar_cliente'),

=======
    # URL borrar producto
    path('productos/<int:pk>/delete/', DeleteProductoView.as_view(), name='borrar_producto'),
    # URL borrar cliente
    path('clientes/<int:pk>/delete/', DeleteClienteView.as_view(), name='borrar_clientes'),
    # URL borrar pedido
    path('pedidos/<int:pk>/delete/', DeletePedidoView.as_view(), name='borrar_pedidos')
>>>>>>> 2c3aeff862fb84e121d835ec1bfa63948475056b
]

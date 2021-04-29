from django.urls import path
from . import views
from appEntrega.views import PedidoDetailView, PedidoListView,CreateProductoView,CreateClienteView,CreateComponenteView, CreatePedidoView, ClienteDetailView, ClienteListView, ProductoListView, ProductoDetailView, DeleteProductoView

urlpatterns = [
    # URL detalle pedido
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='detallePedido'),
    # URL lista pedidos
    path('pedidos/', PedidoListView.as_view(), name='listaPedido'),
    # URL detalle cliente
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name='detalleCliente'),
    # URL lista clientes
    path('clientes/', ClienteListView.as_view(), name='listaCliente'),
    # URL detalle producto
    path('productos/<int:pk>', ProductoDetailView.as_view(), name='detalleProducto'),
    # URL lista productos
    path('productos/', ProductoListView.as_view(), name='listaProducto'),
    #URL nuevo producto
    path('productos/nuevo/', views.CreateProductoView.as_view(), name='producto_form'),
    #URL nuevo cliente
    path('clientes/nuevo/', views.CreateClienteView.as_view(), name='cliente_form'),
    #URL nuevo componente
    path('componentes/nuevo/', views.CreateComponenteView.as_view(), name='componente_form'),
    #URL nuevo orden_pedido
    path('pedidos/nuevo/', views.CreatePedidoView.as_view(), name='pedido_form'),
    #URL borrar producto
    path('productos/<int:pk>/delete/', DeleteProductoView.as_view(),name='borrar_producto')
]

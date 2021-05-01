from django.urls import path
from . import views
from appEntrega.views import PedidoDetailView, PedidoListView, CreateProductoView, CreateClienteView, \
    CreateComponenteView, CreatePedidoView, ClienteDetailView, ClienteListView, ProductoListView, ProductoDetailView, \
    DeleteProductoView, DeletePedidoView, DeleteClienteView, Index,UpdateClienteView,UpdatePedidoView,UpdateProductoView, \
    CreateFacturaView, DeleteFacturaView, DeleteComponenteView, UpdateComponenteView, UpdateFacturaView,\
    FacturaListView, FacturaDetailView

urlpatterns = [
    path('', Index, name='index'),
    #URL LISTA
    # URL lista pedidos
    path('pedidos/', PedidoListView.as_view(), name='listaPedido'),
    # URL lista clientes
    path('clientes/', ClienteListView.as_view(), name='listaCliente'),
    # URL lista productos
    path('productos/', ProductoListView.as_view(), name='listaProducto'),
    # URL lista productos
    path('facturas/', FacturaListView.as_view(), name='listaFacturas'),

    # URL Detalle
    # URL detalle pedido
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='detallePedido'),
    # URL detalle cliente
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name='detalleCliente'),
    # URL detalle producto
    path('productos/<str:pk>', ProductoDetailView.as_view(), name='detalleProducto'),
    # URL detalle factura
    path('facturas/<str:pk>', FacturaDetailView.as_view(), name='detalleFactura'),
    


    #CREAR  /nuevo/
    # URL nueva factura
    path('facturas/nuevo/', views.CreateFacturaView.as_view(), name='factura_form'),
    # URL nuevo producto
    path('productos/nuevo/', views.CreateProductoView.as_view(), name='producto_form'),
    # URL nuevo cliente
    path('clientes/nuevo/', views.CreateClienteView.as_view(), name='cliente_form'),
    # URL nuevo componente
    path('componentes/nuevo/', views.CreateComponenteView.as_view(), name='componente_form'),
    # URL nuevo orden_pedido
    path('pedidos/nuevo/', views.CreatePedidoView.as_view(), name='pedido_form'),


    #BORRAR /delete/
    #URL borrar producto
    path('productos/<str:pk>/delete/', DeleteProductoView.as_view(),name='borrar_producto'),
    #URL borrar cliente
    path('clientes/<int:pk>/delete/', DeleteClienteView.as_view(),name='borrar_clientes'),
    #URL borrar pedido
    path('pedidos/<int:pk>/delete/', DeletePedidoView.as_view(),name='borrar_pedidos'),
    #URL borrar factura
    path('facturas/<int:pk>/delete/', DeleteFacturaView.as_view(),name='borrar_facturas'),
    #URL borrar componente
    path('componente/<int:pk>/delete/', DeleteComponenteView.as_view(),name='borrar_componentes'),

    # EDITAR /editar/
    #URL editar cliente
    path('clientes/<pk>/editar', UpdateClienteView.as_view(),name='editar_cliente'),
    #URL editar cliente
    path('productos/<pk>/editar/', UpdateProductoView.as_view(),name='editar_producto'),
    #URL editar cliente
    path('pedidos/<pk>/editar/', UpdatePedidoView.as_view(),name='editar_pedido'),
    #URL editar cliente
    path('componentes/<pk>/editar/', UpdateComponenteView.as_view(),name='editar_componente'),
    #URL editar cliente
    path('facturas/<pk>/editar/', UpdateFacturaView.as_view(),name='editar_factura'),


]

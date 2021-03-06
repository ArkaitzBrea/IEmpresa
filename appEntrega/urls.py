from django.urls import path
from . import views
from appEntrega.views import PedidoDetailView, PedidoListView, CreateProductoView, CreateClienteView, \
    CreateComponenteView, CreatePedidoView, ClienteDetailView, ClienteListView, ProductoListView, ProductoDetailView, \
    ComponenteListView, \
    DeleteProductoView, DeletePedidoView, DeleteClienteView, DeleteComponenteProductView, DeleteFacturaProductView, \
    Index, UpdateClienteView, contactoView, settingsView,\
    CreateFacturaView, DeleteFacturaView, DeleteComponenteView, UpdateComponenteView, UpdateFacturaView, \
    FacturaListView, FacturaDetailView

urlpatterns = [
    path('', Index, name='index'),
    # URL LISTA
    # URL lista pedidos
    path('pedidos/', PedidoListView.as_view(), name='listaPedido'),
    # URL lista clientes
    path('clientes/', ClienteListView.as_view(), name='listaCliente'),
    # URL lista productos
    path('productos/', ProductoListView.as_view(), name='listaProducto'),
    path('productos-json/', views.getProducts, name='listaProducto1'),
    # URL lista compoentes
    path('componentes/', ComponenteListView.as_view(), name='listaComponente'),
    # URL lista productos
    path('facturas/', FacturaListView.as_view(), name='listaFactura'),

    # URL Detalle
    # URL detalle pedido
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='detallePedido'),
    # URL detalle cliente
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name='detalleCliente'),
    # URL detalle producto
    path('productos/<str:pk>', ProductoDetailView.as_view(), name='detalleProducto'),
    # URL detalle factura
    path('facturas/<str:pk>', FacturaDetailView.as_view(), name='detalleFactura'),

    # CREAR  /nuevo/
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

    # BORRAR /delete/
    # URL borrar producto
    path('productos/<str:pk>/delete/', DeleteProductoView.as_view(), name='borrar_producto'),
    # URL borrar cliente
    path('clientes/<str:pk>/delete/', DeleteClienteView.as_view(), name='borrar_clientes'),
    # URL borrar pedido
    path('pedidos/<str:pk>/delete/', DeletePedidoView.as_view(), name='borrar_pedidos'),
    # URL borrar factura
    path('factura/<str:pk>/delete/', DeleteFacturaView.as_view(), name='borrar_facturas'),
    # URL borrar factura desde pedidoview
    path('pedidos/factura/<str:pk>/delete/', DeleteFacturaProductView.as_view(), name='borrar_factura_producto'),
    # URL borrar componente desde productoview
    path('productos/componente/<int:pk>/delete/', DeleteComponenteProductView.as_view(), name='borrar_componente_producto'),
    # URL borrar componente
    path('componente/<int:pk>/delete/', DeleteComponenteView.as_view(), name='borrar_componentes'),

    # EDITAR /editar/
    # URL editar cliente
    path('clientes/<str:pk>/editar/', UpdateClienteView.as_view(), name='editar_cliente'),
    # URL editar producto
    path('productos/<str:pk>/editar/', views.UpdateProductoView.as_view(), name='editar_producto'),
    # URL editar pedido
    path('pedidos/<str:pk>/editar/', views.UpdatePedidoView.as_view(), name='editar_pedido'),
    # URL editar componente
    path('componentes/<int:pk>/editar/', UpdateComponenteView.as_view(), name='editar_componente'),
    # URL editar factura
    path('facturas/<str:pk>/editar/', UpdateFacturaView.as_view(), name='editar_factura'),

    # URL Configuraci??n de vista
    path('configuracion/', settingsView, name='ConfiguracionView'),

    # URL contactoView
    path('contacto/', contactoView, name='ContactoView'),

]

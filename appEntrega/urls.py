from django.urls import path
from . import views
from appEntrega.views import PedidoDetailView, PedidoListView,CreateProductoView,CreateClienteView,CreateComponenteView, CreatePedidoView

urlpatterns = [
    path('pedidos/<int:pk>', PedidoListView.as_view(), name='detallePedido'),

    #URL nuevo producto
    path('producto/nuevo/', views.CreateProductoView.as_view(), name='producto_form'),
    #URL nuevo cliente
    path('cliente/nuevo/', views.CreateClienteView.as_view(), name='cliente_form'),
    #URL nuevo componente
    path('componente/nuevo/', views.CreateComponenteView.as_view(), name='componente_form'),
    #URL nuevo orden_pedido
    path('pedido/nuevo/', views.CreatePedidoView.as_view(), name='pedido_form'),
]

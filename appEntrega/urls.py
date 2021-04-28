from django.urls import path
from . import views
from appEntrega.views import PedidoDetailView, PedidoListView,CreateProductoView

urlpatterns = [
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='detallePedido'),
    path('producto/nuevo/', views.CreateProductoView.as_view(), name='producto_form'),
    path('producto/nuevo/post_producto/', CreateProductoView.as_view(), name ='post_producto')
]

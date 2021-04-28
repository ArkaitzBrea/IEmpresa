from django.urls import path
from . import views
from appEntrega.views import PedidoDetailView, PedidoListView,CreateNoticiaView

urlpatterns = [
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='detallePedido'),
    path('producto/nuevo/', views.CreateNoticiaView.as_view(), name='producto_form'),
    path('producto/nuevo/post_producto/', CreateNoticiaView.as_view(), name ='post_producto')
]

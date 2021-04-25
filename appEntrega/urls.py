from django.urls import path
from . import views
from appEntrega.views import PedidoDetailView, PedidoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='detallePedido'),
]

from django.urls import path
from .views import OrderViewSet, OrderStatsView

app_name = 'orders_api'

urlpatterns = [
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='orders-list'),
    path('orders-stats/', OrderStatsView.as_view(), name='orders-stats'),
]
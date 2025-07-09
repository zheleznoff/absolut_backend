from django.urls import path
from .views import OrderStatusListView, OrderStatusDetailView

app_name = 'order_statuses_api'

urlpatterns = [
    path('order-statuses/', OrderStatusListView.as_view(), name='order-status-list'),
    path('order-statuses/<int:pk>/', OrderStatusDetailView.as_view(), name='order-status-detail'),
]
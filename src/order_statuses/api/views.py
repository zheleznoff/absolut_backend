from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from order_statuses.models import OrderStatus
from .serializers import OrderStatusSerializer


class OrderStatusListView(generics.ListAPIView):
    """Представление для получения списка всех статусов заказа"""
    queryset = OrderStatus.objects.filter(is_active=True)
    serializer_class = OrderStatusSerializer
    permission_classes = [IsAuthenticated]


class OrderStatusDetailView(generics.RetrieveAPIView):
    """Представление для получения детальной информации о статусе заказа"""
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [IsAuthenticated]
from rest_framework import serializers
from order_statuses.models import OrderStatus


class OrderStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели OrderStatus"""

    class Meta:
        model = OrderStatus
        fields = ['id', 'name', 'description', 'color', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
from rest_framework import serializers
from transport.models import Transport


class TransportSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Transport"""
    
    class Meta:
        model = Transport
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
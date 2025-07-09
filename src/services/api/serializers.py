from rest_framework import serializers
from services.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Service"""

    class Meta:
        model = Service
        fields = ["id", "name", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

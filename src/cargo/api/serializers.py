from rest_framework import serializers
from cargo.models import Cargo


class CargoSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Cargo"""

    class Meta:
        model = Cargo
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
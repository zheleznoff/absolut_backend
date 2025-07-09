from rest_framework import serializers
from packaging.models import Packaging


class PackagingSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Packaging"""
    
    class Meta:
        model = Packaging
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
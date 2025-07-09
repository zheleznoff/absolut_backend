from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    service_names = serializers.SerializerMethodField()
    transport_name = serializers.SerializerMethodField()

    def get_service_names(self, obj):
        return [service.name for service in obj.services.all()]

    def get_transport_name(self, obj):
        return obj.transport.name if obj.transport else None

    class Meta:
        model = Order
        fields = "__all__"
        extra_fields = ['transport_name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['transport_name'] = self.get_transport_name(instance)
        return rep

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from transport.models import Transport
from .serializers import TransportSerializer


class TransportListView(generics.ListAPIView):
    """Представление для получения списка всех транспортных средств"""
    queryset = Transport.objects.filter(is_active=True)
    serializer_class = TransportSerializer
    permission_classes = [IsAuthenticated]


class TransportDetailView(generics.RetrieveAPIView):
    """Представление для получения детальной информации о транспортном средстве"""
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [IsAuthenticated]
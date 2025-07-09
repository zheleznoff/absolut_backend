from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from services.models import Service
from .serializers import ServiceSerializer


class ServiceListView(generics.ListAPIView):
    """Представление для получения списка всех услуг"""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    pagination_class = None


class ServiceDetailView(generics.RetrieveAPIView):
    """Представление для получения детальной информации об услуге"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
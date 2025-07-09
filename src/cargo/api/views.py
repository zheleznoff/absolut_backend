from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from cargo.models import Cargo
from .serializers import CargoSerializer


class CargoListView(generics.ListAPIView):
    """Представление для получения списка всех типов груза"""
    queryset = Cargo.objects.filter(is_active=True)
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]


class CargoDetailView(generics.RetrieveAPIView):
    """Представление для получения детальной информации о типе груза"""
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]
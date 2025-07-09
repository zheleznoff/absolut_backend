from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from packaging.models import Packaging
from .serializers import PackagingSerializer


class PackagingListView(generics.ListAPIView):
    """Представление для получения списка всех типов упаковки"""
    queryset = Packaging.objects.filter(is_active=True)
    serializer_class = PackagingSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['name']


class PackagingDetailView(generics.RetrieveAPIView):
    """Представление для получения детальной информации о типе упаковки"""
    queryset = Packaging.objects.all()
    serializer_class = PackagingSerializer
    permission_classes = [IsAuthenticated]
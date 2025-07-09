import django_filters
from django.db.models import Count
from django.db.models.functions import TruncDate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from orders.api.serializers import OrderSerializer
from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    """Фильтр для заказов"""

    delivery_date = django_filters.DateFilter(field_name="delivery_datetime__date")
    delivery_date__gte = django_filters.DateFilter(
        field_name="delivery_datetime__date", lookup_expr="gte"
    )
    delivery_date__lte = django_filters.DateFilter(
        field_name="delivery_datetime__date", lookup_expr="lte"
    )
    delivery_date_range = django_filters.DateFromToRangeFilter(field_name="delivery_datetime__date")
    services__in = django_filters.BaseInFilter(field_name="services", lookup_expr="in")

    class Meta:
        model = Order
        fields = ["services__in"]


class OrderFilterMixin:
    """Миксин для общей фильтрации заказов"""

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = OrderFilter
    search_fields = ["pk"]
    ordering_fields = ["pk", "delivery_datetime", "transport", "distance"]


class OrderViewSet(OrderFilterMixin, viewsets.ModelViewSet):
    """Вьюсет для заказов"""

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.select_related("transport").prefetch_related("services")


class OrderStatsView(OrderFilterMixin, GenericAPIView):
    """Статистика заказов по дням"""

    def get_queryset(self):
        return Order.objects.all()

    def get(self, request, *args, **kwargs):
        filtered_queryset = self.filter_queryset(self.get_queryset())

        stats = (
            filtered_queryset.annotate(date=TruncDate("delivery_datetime"))
            .values("date")
            .annotate(count=Count("id"))
            .order_by("date")
        )

        data = []
        for item in stats:
            if item["date"]:
                data.append({"date": item["date"].strftime("%Y-%m-%d"), "count": item["count"]})

        return Response(data)

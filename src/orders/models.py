from django.conf import settings
from django.db import models
from order_statuses.models import OrderStatus
from packaging.models import Packaging
from services.models import Service
from transport.models import Transport


class Order(models.Model):
    """
    Модель заказа
    """

    transport = models.ForeignKey(
        Transport, on_delete=models.PROTECT, verbose_name="Модель автомобиля"
    )
    car_number = models.CharField(max_length=32, verbose_name="Номер автомобиля")
    departure_datetime = models.DateTimeField(verbose_name="Дата отправки")
    delivery_datetime = models.DateTimeField(verbose_name="Дата доставки")
    travel_time = models.DurationField(verbose_name="Время в пути")
    distance = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Дистанция (км)")
    media_file = models.FileField(
        upload_to="orders/", blank=True, null=True, verbose_name="Медиафайл (pdf/img)"
    )
    services = models.ManyToManyField(
        Service, related_name="orders_services", verbose_name="Услуги"
    )
    status = models.ForeignKey(
        OrderStatus, on_delete=models.PROTECT, verbose_name="Статус доставки"
    )
    packagings = models.ManyToManyField(
        Packaging, related_name="orders_packagings", verbose_name="Упаковки"
    )
    collector = models.CharField(max_length=70, verbose_name="Сборщик")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ #{self.pk} от {self.created_at.strftime('%Y-%m-%d %H:%M')}"

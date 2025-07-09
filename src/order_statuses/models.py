from django.db import models
from .choices import ColorChoices


class OrderStatus(models.Model):
    """Модель статуса доставки"""

    name = models.CharField(max_length=100, verbose_name="Название статуса")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    color = models.CharField(
        max_length=7,
        default=ColorChoices.GREEN,
        choices=ColorChoices.choices,
        verbose_name="Цвет статуса",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Статус доставки"
        verbose_name_plural = "Статусы доставки"
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

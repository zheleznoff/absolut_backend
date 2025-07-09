from django.db import models


class Cargo(models.Model):
    """Модель типа груза"""
    name = models.CharField(max_length=100, verbose_name="Название типа груза")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Тип груза"
        verbose_name_plural = "Типы груза"
        ordering = ['name']

    def __str__(self):
        return str(self.name)

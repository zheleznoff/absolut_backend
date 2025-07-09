from django.db import models


class Packaging(models.Model):
    """Модель типа упаковки"""
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Тип упаковки"
        verbose_name_plural = "Типы упаковки"
        ordering = ['name']

    def __str__(self):
        return str(self.name)

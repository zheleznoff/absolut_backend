from django.db import models


class Service(models.Model):
    """Модель услуги доставки"""
    name = models.CharField(max_length=100, verbose_name="Название услуги")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['name']

    def __str__(self):
        return str(self.name)

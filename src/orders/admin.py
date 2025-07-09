from django.contrib import admin
from django.utils.html import format_html
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для заказов"""
    list_display = [
        "id",
        "car_number",
        "transport",
        "status_with_color",
        "departure_datetime",
        "delivery_datetime",
        "collector",
        "distance",
        "created_at",
    ]
    list_filter = [
        "status",
        "transport",
        "departure_datetime",
        "delivery_datetime",
        "created_at",
        "services",
        "packagings",
    ]
    search_fields = ["car_number", "collector", "comment", "transport__name", "status__name"]
    readonly_fields = ["created_at", "travel_time_display"]
    filter_horizontal = ["services", "packagings"]
    date_hierarchy = "created_at"
    list_per_page = 25
    list_select_related = ["transport", "status"]

    fieldsets = (
        ("Основная информация", {"fields": ("transport", "car_number", "collector", "status")}),
        (
            "Время и маршрут",
            {
                "fields": (
                    "departure_datetime",
                    "delivery_datetime",
                    "travel_time_display",
                    "distance",
                )
            },
        ),
        ("Услуги и упаковки", {"fields": ("services", "packagings"), "classes": ("collapse",)}),
        (
            "Дополнительно",
            {"fields": ("media_file", "comment", "created_at"), "classes": ("collapse",)},
        ),
    )

    def status_with_color(self, obj):
        """Отображение статуса с цветом"""
        if obj.status:
            color = obj.status.color
            return format_html(
                '<span style="color: {}; font-weight: bold;">{}</span>', color, obj.status.name
            )
        return "-"

    status_with_color.short_description = "Статус"
    status_with_color.admin_order_field = "status__name"

    def travel_time_display(self, obj):
        """Отображение времени в пути в читаемом формате"""
        if obj.travel_time:
            total_seconds = int(obj.travel_time.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            return f"{hours}ч {minutes}м"
        return "-"

    travel_time_display.short_description = "Время в пути"

    def get_queryset(self, request):
        """Оптимизация запросов"""
        return super().get_queryset(request).prefetch_related("services", "packagings")

    def save_model(self, request, obj, form, change):
        """Автоматический расчет времени в пути при сохранении"""
        if obj.departure_datetime and obj.delivery_datetime:
            from datetime import datetime

            if obj.delivery_datetime > obj.departure_datetime:
                obj.travel_time = obj.delivery_datetime - obj.departure_datetime
        super().save_model(request, obj, form, change)

    actions = ["mark_as_completed", "mark_as_in_progress"]

    def mark_as_completed(self, request, queryset):
        """Действие: отметить как завершенные"""
        try:
            from order_statuses.models import OrderStatus

            completed_status = OrderStatus.objects.filter(name__icontains="завершен").first()  # type: ignore
            if completed_status:
                updated = queryset.update(status=completed_status)
                self.message_user(request, f"Успешно обновлено {updated} заказов")
            else:
                self.message_user(
                    request,
                    'Статус "Завершен" не найден. Создайте его в админке статусов.',
                    level=30,  # WARNING level
                )
        except Exception as e:
            self.message_user(
                request,
                f"Ошибка при обновлении статуса: {str(e)}",
                level=40,  # ERROR level
            )

    mark_as_completed.short_description = "Отметить как завершенные"

    def mark_as_in_progress(self, request, queryset):
        """Действие: отметить как в работе"""
        try:
            from order_statuses.models import OrderStatus

            in_progress_status = OrderStatus.objects.filter(name__icontains="в работе").first()  # type: ignore
            if in_progress_status:
                updated = queryset.update(status=in_progress_status)
                self.message_user(request, f"Успешно обновлено {updated} заказов")
            else:
                self.message_user(
                    request,
                    'Статус "В работе" не найден. Создайте его в админке статусов.',
                    level=30,  # WARNING level
                )
        except Exception as e:
            self.message_user(
                request,
                f"Ошибка при обновлении статуса: {str(e)}",
                level=40,  # ERROR level
            )

    mark_as_in_progress.short_description = "Отметить как в работе"

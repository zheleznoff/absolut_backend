from django.urls import path
from .views import ServiceListView, ServiceDetailView

app_name = 'services_api'

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
]
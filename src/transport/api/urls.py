from django.urls import path
from .views import TransportListView, TransportDetailView

app_name = 'transport_api'

urlpatterns = [
    path('transport/', TransportListView.as_view(), name='transport-list'),
    path('transport/<int:pk>/', TransportDetailView.as_view(), name='transport-detail'),
]
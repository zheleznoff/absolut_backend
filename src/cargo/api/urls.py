from django.urls import path
from .views import CargoListView, CargoDetailView

app_name = 'cargo_api'

urlpatterns = [
    path('cargo/', CargoListView.as_view(), name='cargo-list'),
    path('cargo/<int:pk>/', CargoDetailView.as_view(), name='cargo-detail'),
]

from django.urls import path
from .views import PackagingListView, PackagingDetailView

app_name = 'packaging_api'

urlpatterns = [
    path('packaging/', PackagingListView.as_view(), name='packaging-list'),
    path('packaging/<int:pk>/', PackagingDetailView.as_view(), name='packaging-detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    # API لـ عرض الوحدات وإنشاء وحدة جديدة
    path('units/', views.UnitListCreateAPIView.as_view(), name='unit-list-create'),
    # API لـ عرض وتحديث وحذف وحدة معينة
    path('units/<int:pk>/', views.UnitDetailAPIView.as_view(), name='unit-detail'),
    
    # API لـ عرض الخدمات وإنشاء خدمة جديدة
    path('unit_services/', views.UnitServiceListCreateAPIView.as_view(), name='unit-service-list-create'),
    # API لـ عرض وتحديث وحذف خدمة معينة
    path('unit_services/<int:pk>/', views.UnitServiceDetailAPIView.as_view(), name='unit-service-detail'),
]

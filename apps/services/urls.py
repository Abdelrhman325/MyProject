from django.urls import path
from . import views

urlpatterns = [
    # API لـ عرض الوحدات وإنشاء وحدة جديدة
    path('section/', views.SectionListCreateAPIView.as_view(), name='section-list-create'),
    # API لـ عرض وتحديث وحذف وحدة معينة
    path('section/<int:pk>/', views.SectionDetailAPIView.as_view(), name='section-detail'),
    
    # API لـ عرض الخدمات وإنشاء خدمة جديدة
    path('Service/', views.ServiceListCreateAPIView.as_view(), name='unit-service-list-create'),
    # API لـ عرض وتحديث وحذف خدمة معينة
    path('Service/<int:pk>/', views.ServiceDetailAPIView.as_view(), name='unit-service-detail'),
]

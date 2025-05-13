# studentportal/urls.py
from django.urls import path
from .views import AllNotificationsView, CreateNotificationView, DeleteNotificationView, StudentPortalAPIView, UpdateNotificationView, UserNotificationsView

urlpatterns = [
    path('portal/', StudentPortalAPIView.as_view()),              # list + create
    path('portal/<int:pk>/', StudentPortalAPIView.as_view()),     # detail, update, delete
    
    
    
     path('notifications/', CreateNotificationView.as_view(), name='create-notification'),
    path('mynotifications/', UserNotificationsView.as_view(), name='user-notifications'),
    path('allnotifications/', AllNotificationsView.as_view(), name='all-notifications'),
    path('update/<int:pk>/', UpdateNotificationView.as_view(), name='update-notification'),
    path('delete/<int:pk>/', DeleteNotificationView.as_view(), name='delete-notification'),
]

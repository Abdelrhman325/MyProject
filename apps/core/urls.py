from django.urls import path
from . import views

urlpatterns = [
    # API URLs for VisionMission
    path('vision-mission/', views.VisionMissionView.as_view(), name='vision-mission-list'),
    path('vision-mission/<int:pk>/', views.VisionMissionView.as_view(), name='vision-mission-detail'),

    # API URLs for Slider
    path('slider/', views.SliderView.as_view(), name='slider-list'),
    path('slider/<int:pk>/', views.SliderView.as_view(), name='slider-detail'),

    # API URLs for FacultyInfo
    path('faculty-info/', views.FacultyInfoView.as_view(), name='faculty-info-list'),
    path('faculty-info/<int:pk>/', views.FacultyInfoView.as_view(), name='faculty-info-detail'),

    # API URLs for Statistics
    path('statistics/', views.StatisticsView.as_view(), name='statistics-list'),
    path('statistics/<int:pk>/', views.StatisticsView.as_view(), name='statistics-detail'),

    # API URLs for Collegeleaders
    path('college-leaders/', views.CollegeLeadersView.as_view(), name='college-leaders-list'),
    path('college-leaders/<int:pk>/', views.CollegeLeadersView.as_view(), name='college-leaders-detail'),
    
    #مقترحات وشكاوى
     path('complaints/create/', views.CreateComplaintView.as_view(), name='create-complaint'),
    path('complaints/', views.ListComplaintsView.as_view(), name='list-complaints'),
    path('complaints/<int:pk>/update/', views.UpdateComplaintView.as_view(), name='update-complaint'),
    path('complaints/<int:pk>/respond/', views.AdminRespondComplaintView.as_view(), name='respond-complaint'),
]

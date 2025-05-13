from django.urls import path
from .views import (
    DepartmentListCreateAPIView, DepartmentRetrieveUpdateDestroyAPIView,
    SpecialProgramListCreateAPIView, SpecialProgramRetrieveUpdateDestroyAPIView,
    MastersProgramListCreateAPIView, MastersProgramRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Departments
    path('departments/', DepartmentListCreateAPIView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyAPIView.as_view(), name='department-retrieve-update-destroy'),

    # Special Programs
    path('specialprograms/', SpecialProgramListCreateAPIView.as_view(), name='specialprogram-list-create'),
    path('specialprograms/<int:pk>/', SpecialProgramRetrieveUpdateDestroyAPIView.as_view(), name='specialprogram-retrieve-update-destroy'),

    # Masters Programs
    path('mastersprograms/', MastersProgramListCreateAPIView.as_view(), name='mastersprogram-list-create'),
    path('mastersprograms/<int:pk>/', MastersProgramRetrieveUpdateDestroyAPIView.as_view(), name='mastersprogram-retrieve-update-destroy'),
]

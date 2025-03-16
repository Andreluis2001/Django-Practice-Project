from django.urls import path
from . import views

urlpatterns = [
    path('machines/', views.MachineListAPIView.as_view()),
    path('machines/<int:pk>/', views.MachineDetailAPIView.as_view()),
    path('technicians/', views.TechnicianListAPIView.as_view()),
    path('technicians/<int:pk>/', views.TechnicianDetailAPIView.as_view()),
    path('maintenances/', views.MaintenanceListAPIView.as_view()),
    path('maintenances/<int:pk>/', views.MaintenanceDetailAPIView.as_view()),
]
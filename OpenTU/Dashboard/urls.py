from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_request, name='dashboard'),
    path('edit_info/', views.edit_info, name='edit_info'),
]
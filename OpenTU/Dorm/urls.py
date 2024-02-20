from django.urls import path
from . import views

urlpatterns = [
    path('dorm/', views.dorm_request, name='dorm'),
]
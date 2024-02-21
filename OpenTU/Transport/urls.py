from django.urls import path
from . import views

urlpatterns = [
    path('transport/', views.transport_request, name='transport'),
]
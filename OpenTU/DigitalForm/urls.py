from django.urls import path
from . import views

urlpatterns = [
    path('digital_form/', views.digital_form_request, name='digital_form'),
]
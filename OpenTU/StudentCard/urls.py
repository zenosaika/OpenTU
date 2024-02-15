from django.urls import path
from . import views

urlpatterns = [
    path('idcard/', views.idcard_request, name='idcard'),
]
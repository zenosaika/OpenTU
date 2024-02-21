from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library_request, name='library'),
    path('borrow/<int:id>', views.borrow, name='borrow'),
]
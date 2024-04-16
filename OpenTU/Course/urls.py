from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.schedule_request, name='schedule'),
    path('manage_course/', views.manage_course_request, name='manage_course'),
    path('unenroll/<int:id>', views.unenroll_request, name='unenroll'),
    path('enroll/<int:id>', views.enroll_request, name='enroll'),
]
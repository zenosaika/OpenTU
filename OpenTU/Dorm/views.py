from django.shortcuts import render
from .models import Room, Bill

def dorm_request(request):
    room = Room.objects.filter()
    return render(request, 'Dorm/dorm.html', {})
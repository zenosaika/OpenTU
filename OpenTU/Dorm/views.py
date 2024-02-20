from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from User.models import Student
from .models import Room, Bill

@login_required
def dorm_request(request):
    student = Student.objects.filter(user=request.user)
    context = {}
    if student:
        room_id = student[0].room.pk
        if room_id:
            room = Room.objects.filter(pk=room_id)
            bills = Bill.objects.filter(room_id=room_id)

            context['roommates'] = Student.objects.filter(room=room_id)
            context['electric_cost'] = sum(bill.electric_cost for bill in bills if bill.payment_status==False)
            context['water_cost'] = sum(bill.water_cost for bill in bills if bill.payment_status==False)

    return render(request, 'Dorm/dorm.html', context)

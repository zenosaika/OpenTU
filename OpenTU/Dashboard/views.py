from django.shortcuts import render
from User.models import Student

def dashboard_request(request):
    student = Student.objects.filter(user=request.user)
    context = {}
    if student:
        context['student'] = student[0]
    else:
        # create new Student object for this user
        # go to new Student form
        ...
    return render(request, 'Dashboard/dashboard.html', context)
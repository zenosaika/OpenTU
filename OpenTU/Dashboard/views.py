from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from User.models import Student
from User.forms import StudentForm
import datetime


@login_required
def dashboard_request(request):
    student = Student.objects.filter(user=request.user)
    context = {}
    if student:
        context['student'] = student[0]

        # upcoming events
        events = []
        today = datetime.datetime.today() + datetime.timedelta(hours=7)
        today_day = (today).weekday()
        for course in student[0].enrolled_courses.all():
            if int(course.class_day) == today_day:
                events.append({
                    'description': f'{course.short_name} @ {course.room}',
                    'time': course.class_start.strftime('Today %H:%M'),
                    'compareval': datetime.datetime.combine(datetime.date(year=2003, month=7, day=10), course.class_start)
                })

        context['events'] = sorted(events, key=lambda event: event['compareval'])
            
    return render(request, 'Dashboard/dashboard.html', context)

@login_required
def edit_info(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            student = Student.objects.get(user=request.user)
            if student:
                student.first_name = form.first_name
                student.last_name = form.last_name
                student.email = form.email
                student.phone = form.phone
                student.image = form.image
                student.save()

            return redirect('/dashboard')
    else:
        context = {'form': StudentForm()}
        return render(request, 'Dashboard/edit_info.html', context)
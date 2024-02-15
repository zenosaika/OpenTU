from django.shortcuts import render
from User.models import Student

DAYS_OF_WEEK = {
    '0': 'MON',
    '1': 'TUE',
    '2': 'WED',
    '3': 'THU',
    '4': 'FRI',
    '5': 'SAT',
    '6': 'SUN',
}

def schedule_request(request):
    student = Student.objects.filter(user=request.user)
    context = {'enrolled_courses': []}
    if student:
        enrolled_courses = student[0].enrolled_courses.all()
        for course in enrolled_courses:
            course.schedule = f"{DAYS_OF_WEEK[course.class_day]} | {course.class_start.strftime('%H:%M')} - {course.class_finish.strftime('%H:%M')}"
        context['enrolled_courses'] = enrolled_courses
    return render(request, "Course/schedule.html", context)
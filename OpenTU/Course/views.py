from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from User.models import Student
import datetime

DAYS_OF_WEEK = {
    '0': 'MON',
    '1': 'TUE',
    '2': 'WED',
    '3': 'THU',
    '4': 'FRI',
    '5': 'SAT',
    '6': 'SUN',
}

COLOR_CLASSES = [
    'bg-purple',
    'bg-sky',
    'bg-pink',
    # 'bg-orange',
    'bg-green',
    'bg-yellow',
    # 'bg-lightred',
]

@login_required
def schedule_request(request):
    student = Student.objects.filter(user=request.user)
    context = {'enrolled_courses': []}
    if student:
        enrolled_courses = student[0].enrolled_courses.all()
        for course in enrolled_courses:
            course.schedule = f"{DAYS_OF_WEEK[course.class_day]} | {course.class_start.strftime('%H:%M')} - {course.class_finish.strftime('%H:%M')}"
        context['enrolled_courses'] = enrolled_courses

    # make timeslot
    begin_time = datetime.datetime(year=2003, month=7, day=10, hour=8, minute=30) # 8:30
    end_time = datetime.datetime(year=2003, month=7, day=10, hour=17, minute=00) # 17:00
    time_delta = (end_time - begin_time).total_seconds() // 60
    

    n_slot = 17
    minute_per_slot = time_delta / n_slot

    days = [{'day': day, 'slot': [None for _ in range(n_slot)]} for day in DAYS_OF_WEEK.values()]

    color_index = 0
    for course in enrolled_courses:
        start_datetime = datetime.datetime.combine(datetime.date(year=2003, month=7, day=10), course.class_start)
        finish_datetime = datetime.datetime.combine(datetime.date(year=2003, month=7, day=10), course.class_finish)
        start_index = int((start_datetime - begin_time).total_seconds() // 60 // minute_per_slot)
        class_duration = (finish_datetime - start_datetime).total_seconds() // 60
        for i in range(int(class_duration / minute_per_slot)):
            color = COLOR_CLASSES[color_index%len(COLOR_CLASSES)]
            days[int(course.class_day)]['slot'][start_index+i] = {'subject': course.short_name, 'color': color}
            course.color = color
        color_index += 1

    context['days'] = days

    return render(request, "Course/schedule.html", context)
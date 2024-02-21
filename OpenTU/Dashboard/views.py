from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from User.models import Student
from User.forms import StudentForm

@login_required
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
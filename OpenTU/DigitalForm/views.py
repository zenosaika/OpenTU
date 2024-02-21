from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report

def digital_form_request(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('/digital_form')
    else:
        context = {'form': ReportForm(), 'reports': Report.objects.all()}
        return render(request, 'DigitalForm/digital_form.html', context)
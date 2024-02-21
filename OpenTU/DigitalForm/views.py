from django.shortcuts import render, redirect
from .forms import ReportForm

def digital_form_request(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('/dashboard')
    else:
        context = {'form': ReportForm()}
        return render(request, 'DigitalForm/digital_form.html', context)
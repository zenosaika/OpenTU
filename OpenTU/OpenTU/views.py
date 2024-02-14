from django.shortcuts import render

def homepage(request):
    return render(request, 'OpenTU/homepage.html')
from django.shortcuts import render

def transport_request(request):
    context = {}
    return render(request, 'Transport/transport.html', context)
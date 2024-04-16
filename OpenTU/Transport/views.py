from django.shortcuts import render
from .models import Station, Bus
from datetime import datetime

def transport_request(request):
    context = {}

    stations = Station.objects.all()
    red_stations = []
    yellow_stations = []
    green_stations = []
    purple_stations = []

    for station in stations:
        station.available_buses_list = [b for b in station.available_buses.all()]
        if station.type == 'red':
            red_stations.append(station)
        elif station.type == 'yellow':
            yellow_stations.append(station)
        elif station.type == 'green':
            green_stations.append(station)
        elif station.type == 'purple':
            purple_stations.append(station)

    context['red_stations'] = red_stations
    context['yellow_stations'] = yellow_stations
    context['green_stations'] = green_stations
    context['purple_stations'] = purple_stations

    context['time'] = datetime.now().strftime("%H:%M:%S")

    return render(request, 'Transport/transport.html', context)
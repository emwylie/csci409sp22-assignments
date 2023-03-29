from django.http import HttpResponse
from .models import Flight  # Import Flight model
from airports.models import Airport  # Import airport model to get airport id and code
from .forms import FlightForm
from django.shortcuts import render


def index(request):
    # Fetch all flights
    # flights = Flight.objects.all()
    # flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code for f in flights])
    # return HttpResponse('Listing all flights: ' + flight_list)
    form = FlightForm()
    return render(request, 'flights/index.html', {'form': form})


def flight_search(request, flight_request, flight_origin, flight_destination):
    origin = Airport.objects.get(airport_code=flight_origin)
    destination = Airport.objects.get(airport_code=flight_destination)
    # Code to select flights from the database
    flights = Flight.objects.filter(origin=origin).filter(destination=destination)
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)


def search(request):
    form = FlightForm(request.POST)
    if form.is_valid():
        origin = Airport.objects.get(airport_code=form.cleaned_data['origin'])
        destination = Airport.objects.get(airport_code=form.cleaned_data['destination'])
        # destination = form.cleaned_data['destination']
        flights = Flight.objects.get(origin=origin, destination=destination)
        return render(request, 'flights/flight_search.html', {'flights': flights})

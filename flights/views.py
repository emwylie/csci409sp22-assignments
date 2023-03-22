from django.http import HttpResponse
from .models import Flight # Import Flight model
from airports.models import Airport # Import airport model to get airport id and code

def index(request):
    # Fetch all flights
    flights = Flight.objects.all()
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code for f in flights])
    return HttpResponse('Listing all flights: ' + flight_list)

def flight_search(request, flight_request, flight_origin, flight_destination):
    origin = Airport.objects.get(airport_code=flight_origin)
    destination = Airport.objects.get(airport_code=flight_destination)
    # Code to select flights from the database
    flights = Flight.objects.filter(origin=origin).filter(destination=destination)
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)



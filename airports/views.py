from django.http import HttpResponse
from django.shortcuts import render
from .models import Airport
from .models import Runway

def index(request):
    # Fetch all airports from database
    airports = Airport.objects.all()
    # Place all airports into a context variable for retrieval in the view
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)


def airport_info(request, airport_code):
    # Fetch the airport by a certain code
    # We should use get, only expecting one airport per code
    airports = Airport.objects.filter(airport_code=airport_code)
    # Filter for the airport variables
    # Display airport name and code
    context = {'airports': airports}
    # return HttpResponse('Showing info for airport: ' + airport.name + "- " + airport.airport_code)
    return render(request, 'airports/airport.html', context)

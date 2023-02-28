from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from flights')

def flight_search(request, flight_request, flight_origin, flight_destination):
    return HttpResponse('Showing flights from: ' + flight_origin + ' to ' + flight_destination)

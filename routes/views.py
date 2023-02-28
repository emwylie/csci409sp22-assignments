from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from routes')

def route_search(route_request, route_origin, route_destination):
    return HttpResponse('Showing route from: ' + route_origin + ' to ' + route_destination)

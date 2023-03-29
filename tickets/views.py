from django.http import HttpResponse
from .models import Reservation
from django.shortcuts import render
from .forms import TicketForm

def index(request):
    # Create an instance of the form class
    form = TicketForm()
    # Render the form
    return render(request, 'tickets/index.html', {'form': form})
    # return HttpResponse('Hello from tickets')

def ticket_search(request, confirmation_number):
    # Select the singular reservation for the confirmation number
    # Note: the confirmation_number is the id in the Reservation table
    reservation = Reservation.objects.get(id=confirmation_number)
    return HttpResponse('Number of tickets for confirmation number: ' + str(confirmation_number) + " is " +
                        str(reservation.num_people))



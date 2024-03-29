# Load path from django.urls
from django.urls import path

import airports
# Load applications views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index view
    # Example url: /airports/
    path('/', views.index),
    # Show FLight info
    # Example url /flights/search/MYR/ATL
    # the airport_code parameter in the url section
    #   the parameter in the airport_info function
    path('/<confirmation_number>', views.ticket_search),
    path('/search/', airports.views.search),

]

# Load path from django.urls
from django.urls import path
# Load applications views.py file
from . import views

#Define url patterns
urlpatterns = [
    # Get index view
    # Example url: /airports/
    path('/', views.index),
    # Show FLight info
    # Example url /flights/search/MYR/ATL
    # the airport_code parameter in the url section
    #   the parameter in the airport_info function
    path('/<str:airport_code>', views.airport_info),

]
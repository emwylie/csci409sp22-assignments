from django import forms

class FlightForm(forms.Form):
    origin = forms.CharField(label='Origin')
    destination = forms.CharField(label='Destination')

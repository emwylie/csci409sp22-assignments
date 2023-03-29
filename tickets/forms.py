from django import forms

class TicketForm(forms.Form):
    confirmation_number = forms.IntegerField(label='Confirmation Number')
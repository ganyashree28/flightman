from django import forms
from django import forms
from django.core.exceptions import ValidationError
from .models import Flight
from django.utils import timezone
import re

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_number', 'airways_name', 'departure_time', 'ticket_price']
        widgets = {
            'flight_number': forms.TextInput(attrs={
                'pattern': '[A-Z]{2}\d{4}',
                'title': 'Flight number must be in the format: AA1234',
                'required': True
            }),
            'airways_name': forms.TextInput(attrs={
                'required': True,
                'pattern': '[a-zA-Z\s]+',
                'title': 'Airways name must only contain letters and spaces'
            }),
            'departure_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'required': True
            }),
            'ticket_price': forms.NumberInput(attrs={
                'min': 0.01,
                'step': 0.01,
                'required': True,
                'title': 'Ticket price must be a positive number'
            }),
        }

    def clean_flight_number(self):
        flight_number = self.cleaned_data['flight_number']
        if not re.match(r'^[A-Z]{2}\d{4}$', flight_number):
            raise ValidationError('Flight number must be in the format: AA1234')
        return flight_number

    def clean_airways_name(self):
        airways_name = self.cleaned_data['airways_name']
        # Additional validation logic can be added here if needed
        return airways_name

    def clean_departure_time(self):
        departure_time = self.cleaned_data['departure_time']
        if departure_time < timezone.now():
            raise ValidationError('Departure time must be in the future.')
        return departure_time

    def clean_ticket_price(self):
        ticket_price = self.cleaned_data['ticket_price']
        if ticket_price <= 0:
            raise ValidationError('Ticket price must be positive.')
        return ticket_price

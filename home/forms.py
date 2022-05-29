from dataclasses import fields
from django import forms

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
            'p_name':"Patient's Name",
            'p_phone':"Patient's Phone No",
            'p_email':"Patient's Email ID",
            'doc_name':"Doctor's Name",
            'booking_date':"Booking Date"
        }

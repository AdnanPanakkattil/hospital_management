from django import forms

from .models import Booking

class Dateinput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields ='__all__'

        widgets = {
            'booking_date' : Dateinput(),
        }
        
        labels = {
            'p_name':"patient Name:" ,
            'p_email': "patient email",
            'doc_name': 'Doctor name',
            'booking_date ': 'booking Date',
            'p_phone': 'mobile namber'
        }
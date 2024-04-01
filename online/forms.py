from django import forms
from .models import infotech

class BookingForm(forms.ModelForm):
    class Meta:
        model = infotech
        fields = ['firstname', 'secondname', 'mobile1', 'mobile2', 'village', 'district', 'total_days', 'booking_days',]

    # You can also add widgets or customize form fields here if needed

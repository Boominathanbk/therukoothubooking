from django.shortcuts import render
from django.http import HttpResponse
from .models import infotech
from .forms import BookingForm
from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ACbf3f47d47581e42d48ededcaefa73f32'
TWILIO_AUTH_TOKEN = 'd84915d96479267aec3740015dd74544'
TWILIO_PHONE_NUMBER = '+19036237527'

def send_sms(to_number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=+918778604136,
        from_=+19036237527,
        body=message
    )

def create_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            secondname = form.cleaned_data['secondname']
            mobile1 = form.cleaned_data['mobile1']
            mobile2 = form.cleaned_data['mobile2']
            village = form.cleaned_data['village']
            district = form.cleaned_data['district']
            total_days = form.cleaned_data['total_days']
            booking_days = form.cleaned_data['booking_days']


            if infotech.objects.filter(firstname=firstname, secondname=secondname, mobile1=mobile1, mobile2=mobile2,
                                       village=village, district=district, total_days=total_days, booking_days=booking_days ,).exists():
                error_message = 'This date is already booked for the provided firstname. Please choose another date or contact support.'
                return render(request, 'index.html', {'form': form, 'error_message': error_message})
            else:

                new_booking = form.save()
                # Send SMS notification
                booking_message = f'Hello {firstname} {mobile1} {secondname} {mobile2} {booking_days} {village}, your booking with ID {new_booking.id} is confirmed for {total_days} days Therukoothu booking.'
                # Pass mobile1 as the recipient for SMS notification
                send_sms(mobile1, booking_message)
                success_message = 'Booking successful! Your booking ID is: {}'.format(new_booking.id)
                # Clear the form data
                form = BookingForm()
                return render(request, 'index.html', {'form': form, 'success_message': success_message})
        else:
            return render(request, 'index.html', {'form': form})
    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})

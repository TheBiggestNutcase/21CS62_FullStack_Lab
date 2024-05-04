from django.shortcuts import render
from django.utils import timezone

def offset_datetime(request):
    # Get the current date and time
    current_datetime = timezone.now()

    # Calculate the date and time four hours ahead
    four_hours_ahead = current_datetime + timezone.timedelta(hours=4)

    # Calculate the date and time four hours before
    four_hours_before = current_datetime - timezone.timedelta(hours=4)

    # Pass the values to the template
    return render(request, 'offsetdatetime_app/offset_datetime.html', {
        'current_datetime': current_datetime,
        'four_hours_ahead': four_hours_ahead,
        'four_hours_before': four_hours_before
    })

from datetime import datetime
from django.shortcuts import render

from .raspberryPi import raspberryPi_starts


def services(request):
    return render(request, 'services.html', {
        'current_time': str(datetime.now()),
    })

def check_start(request):
    raspberryPi_starts()

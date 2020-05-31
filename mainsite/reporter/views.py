from datetime import datetime
from django.shortcuts import render

from .raspberryPi import raspberryPi_starts


def index(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })

def services(request):
    return render(request, 'services.html', {
        'current_time': str(datetime.now()),
    })

def contact(request):
    return render(request, 'contact.html', {
        'current_time': str(datetime.now()),
    })

def check_start(request):
    raspberryPi_starts()

from datetime import datetime
from django.shortcuts import render

from .register import register
from .log import log
from .track import track


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

def about(request):
    return render(request, 'about.html', {
        'current_time': str(datetime.now()),
        'Items': [{'mood': '5', 'diastolicBP': '120', 'Time': '2020-06-11_15-08-32', 'systolicBP': '80', 'Name': '何沛臻'}, {'mood': '3', 'diastolicBP': '130', 'Time': '2020-06-12_15-08-32', 'systolicBP': '90', 'Name': '何沛臻'}]
    })



def track_start(request):
    track()

def register_start(request):
    register()

def log_start(request):
    log()
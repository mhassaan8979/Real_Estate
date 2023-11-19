from django.http import JsonResponse
from django.shortcuts import render
from .util import *

def home(request):
    load_saved_artifacts()
    location_names = get_location_names()
    estimated_price = None  # Set a default value

    if request.method == 'POST':
        location = request.POST.get('location')
        area = float(request.POST.get('area'))
        bedroom = float(request.POST.get('bedrooms'))
        bath = float(request.POST.get('baths'))
        estimated_price = get_estimated_price(location, area, bedroom, bath)
        
    return render(request, 'home.html', {'location_names': location_names, 'estimated_price': estimated_price})

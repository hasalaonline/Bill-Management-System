import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import CEB,NWSDB
from django.contrib import messages

# Create your views here.
def main(request):
    return render(request,'main.html')

def ceb(request):
    if request.method == 'POST':
        username = request.POST['username']
        month = request.POST['month']
        meter_reading = request.POST['meter_reading']
        monthlyunits = request.POST['units']

        try:
            user = CEB.objects.get(username=username)
            meter_readings = user.meter_readings  # Retrieve the existing data as a dictionary
            units = user.units
        except CEB.DoesNotExist:
            return HttpResponse("Model does not exist.")

        meter_readings[month] = meter_reading  # Perform item assignment on the dictionaries
        units[month] = monthlyunits

        user.save()

        messages.success(request, "You have successfully added your bill")
        return redirect('main')

    return redirect('main')


def nwsdb(request):
    if request.method == 'POST':
        username = request.POST['username']
        month = request.POST['month']
        meter_reading = request.POST['meter_reading']
        monthlyunits = request.POST['units']

        try:
            user = NWSDB.objects.get(username=username)
            meter_readings = user.meter_readings  # Retrieve the existing data as a dictionary
            units = user.units
        except NWSDB.DoesNotExist:
            return HttpResponse("Model does not exist.")

        meter_readings[month] = meter_reading  # Perform item assignment on the dictionaries
        units[month] = monthlyunits

        user.save()

        messages.success(request, "You have successfully added your bill")
        return redirect('main')

    return redirect('main')
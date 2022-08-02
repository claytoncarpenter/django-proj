from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import sensorData, lightData
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')
def r(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'Final_Project_Carpenter.html')

def resume(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'Resume.html')


def addSensorData(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sensor/addSensorData.html')

def showSensorData(request):
   if request.method == 'POST':
      tempr= request.POST["temp"]
      humi = request.POST["hum"]
      reading = sensorData(temp=Decimal(tempr), hum=Decimal(humi))
      reading.save()   
      dict = {
         'tempr': tempr,
         'humi': humi
      }
      return render(request, 'sensor/showSensorData.html', dict) 

@csrf_exempt 
def addLightData(request):
   if request.method == 'GET':
      light= request.GET["brightness"]
      reading = lightData(brightness=int(light))
      reading.save()   
      return render(request, 'index.html') 
from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2

def home(request):
    g = GeoIP2()
    x =g.country('google.com')


    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #if x_forwarded_for:

    #ip = request.META.get('REMOTE_ADDR')
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    y = g.city('183.82.219.109')
    lat, long = g.lat_lon('183.82.219.109')
    context = {'x': x, 'y': y,'ip':ip,'lat':lat,'long':long}
    return render(request,'home.html',context)

# Create your views here.

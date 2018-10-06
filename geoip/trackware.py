from django.contrib.gis.geoip2 import GeoIP2
from geo.models import Log # your simple Log model

def get_ip(request):
   xff = request.META.get('HTTP_X_FORWARDED_FOR')
   if xff:
      return xff.split(',')[0]
   return request.META.get('REMOTE_ADDR')

class UserLocationLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user:
            # Only log requests for superusers,
            # you can control this by adding a setting
            # to track other user types
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            try:
                g = GeoIP2()
                lat,long = g.lat_lon(ip)
                Log.objects.create(request.user, ip, lat, long)
            except:
                pass
        return self.get_response(request)



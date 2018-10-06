from django.db import models

class Log(models.Model):
    user = models.CharField(verbose_name="User",max_length=32)
    ip=models.GenericIPAddressField(verbose_name="IP")
    lat= models.DecimalField(verbose_name="Lat",max_digits=10,decimal_places=1)
    long= models.DecimalField(verbose_name="Long",max_digits=10,decimal_places=1)
# Create your models here.

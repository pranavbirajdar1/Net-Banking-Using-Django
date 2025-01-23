from django.db import models

# Create your models here.


class Otp(models.Model):
    otp = models.CharField(max_length=10 ,verbose_name='OTP')
    
    
    
class EmailPreferences(models.Model):
    email = models.EmailField(max_length=255, unique=True ,null=True ,blank=True, verbose_name='Email')
    preferences = models.CharField(max_length=255, blank=True, null=True , verbose_name='PReferences')
    notifications = models.BooleanField(default=False , verbose_name='Notification Preference')
  
            
            
class SmsAlert(models.Model):
    phone_number = models.CharField(max_length=10, unique=True, verbose_name='Phone Number')
    alert = models.CharField(max_length=255, blank=True, null=True , verbose_name='Alert')
    status = models.BooleanField(default=False , verbose_name='Status')
    
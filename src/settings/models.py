from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class IsAuthenticated(models.Model):
    index = models.BigAutoField(db_index=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Verification', default=1) 
    isverified = models.BooleanField(verbose_name="Is Authenticated  ?" , default=False)
    otp = models.CharField(max_length=6,verbose_name="Otp")
    

 
    
class EmailPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Verification', default=1) 
    email = models.EmailField(max_length=255, unique=True ,null=True ,blank=True, verbose_name='Email')
    preferences = models.CharField(max_length=255, blank=True, null=True , verbose_name='PReferences')
    notifications = models.BooleanField(default=False , verbose_name='Notification Preference')
  
            
            
class SmsAlert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Verification', default=1) 
    phone_number = models.CharField(max_length=10, unique=True, verbose_name='Phone Number')
    alert = models.CharField(max_length=255, blank=True, null=True , verbose_name='Alert')
    status = models.BooleanField(default=False , verbose_name='Status')
    
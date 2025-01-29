from django.db import models
from django.contrib.auth.models import User
# Create your models here.







class ContactPreference(models.Model):
    
    EMAIL_CHOICES = [
        ('all', 'All'),
        ('important', 'Important Only'),
        ('none', 'None'),
    ]
    
    SMS_CHOICES = [
        ('all', 'All'),
        ('important', 'Important Only'),
        ('none', 'None'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Verification', default=1) 
    emailnotification = models.CharField(max_length=30,choices=EMAIL_CHOICES, default="none",verbose_name="Email Notifications")
    smsnotification = models.CharField(max_length=30, choices=SMS_CHOICES ,default="none",verbose_name="SMS Notifications")
   
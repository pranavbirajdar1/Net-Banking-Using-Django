from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile',related_query_name='profile',db_index=True) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',null=True,blank=True,verbose_name='user_profile')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed




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
   
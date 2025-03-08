from django.db import models
from django.contrib.auth.models import User

class IsAuthenticated(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Verification')
    isverified = models.BooleanField(verbose_name="Is Authenticated?", default=False)

    def save(self, *args, **kwargs):
        # Automatically set the isverified field based on the user's authentication status
        self.isverified = self.user.is_authenticated
        super(IsAuthenticated, self).save(*args, **kwargs)  # Call the superclass's save method to save the instance

    def __str__(self):
        return f"{self.user.username} - Verified: {self.isverified}"

    
class EmailPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Verification') 
    email = models.EmailField(max_length=255, unique=True ,null=True ,blank=True, verbose_name='Email')
    preferences = models.CharField(max_length=255, blank=True, null=True , verbose_name='PReferences')
    notifications = models.BooleanField(default=False , verbose_name='Notification Preference')
  
            
            
class SmsAlert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Verification') 
    phone_number = models.CharField(max_length=10, unique=True, verbose_name='Phone Number')
    alert = models.CharField(max_length=255, blank=True, null=True , verbose_name='Alert')
    status = models.BooleanField(default=False , verbose_name='Status')
    
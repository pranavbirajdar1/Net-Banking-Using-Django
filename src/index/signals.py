from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from django.http import HttpRequest
from .models import CustomUserLogin

@receiver(user_logged_in)
def log_user_login(sender, request: HttpRequest, user, **kwargs):
   if sender == User:
        ip_address = request.META.get('REMOTE_ADDR')
        UserLogin.objects.create(
            user=user,
            login_time=now(),
            ip_address=ip_address
        )
        
        print('USER LOGGED.')
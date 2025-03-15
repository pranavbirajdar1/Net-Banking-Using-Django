from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Accbalance
import logging 

logger = logging.getLogger(__name__)
@receiver(post_save, sender=User)
def log_user_login(sender, instance, created, **kwargs):
    if created:
        Accbalance.objects.create(user=instance)
        
        logger.info('USER BALANCE CREATED.')
        print('USER BALANCE CREATED.')
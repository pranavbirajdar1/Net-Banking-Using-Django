from django.db import models

# Create your models here.
class NewsLetter(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    date_subscribed = models.DateTimeField(auto_now=True) 
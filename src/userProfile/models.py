from django.db import models
from model_utils.fields import UUIDField

class MyAppModel(models.Model):
    uuid = UUIDField(primary_key=True, version=4, editable=False)
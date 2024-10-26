from django.urls import path
from .views import *
urlpatterns = [
   path('loan', loan, name='loan'),
]

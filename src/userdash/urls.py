from django.urls import path
from .views import *
urlpatterns = [
    
    path('userdashboard/',userdashboard , name="userdashboard"),
    path('newsletter/',newsletter,name='nletter'),
    
]

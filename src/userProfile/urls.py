from django.urls import path
from .views import *
urlpatterns = [
    
    
   
    path('profile/<int:id>/',profile , name="profile_update"),

    
   
    
]

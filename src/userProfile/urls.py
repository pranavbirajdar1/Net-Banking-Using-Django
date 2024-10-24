from django.urls import path
from .views import *
urlpatterns = [
    
    
    #path('profile/',profile , name="profile"),
    path('profile/<int:id>/',profile , name="profile_update"),
    
   
    
]

from django.urls import path
from .views import *
urlpatterns = [
    
    
   
    path('profile/<int:id>/',profile , name="profile_update"),
    path('profile/update/<int:id>/',update , name="profile_updated"),
    
   
    
]

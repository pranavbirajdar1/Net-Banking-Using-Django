from django.urls import path
from .views import *
urlpatterns = [
    
    
    path('settings/',settings , name="settings"),
    path('set/',set , name="set"),
     path('settings/update/<int:id>/',updated , name="profile_up"),
    path('settings/add-update/<int:id>/',addupdated , name="address_up"),
    path('settings/con-update/<int:id>/',conupdated , name="contact_up"),
   
   
    
]

from django.urls import path
from .views import *
urlpatterns = [
    
    
   
    path('profile/<int:id>/',profile , name="profile_update"),
    path('profile/update/<int:id>/',update , name="profile_updated"),
    path('profile/add-update/<int:id>/',addupdate , name="address_updated"),
    path('profile/con-update/<int:id>/',conupdate , name="contact_updated"),
    
   
    
]

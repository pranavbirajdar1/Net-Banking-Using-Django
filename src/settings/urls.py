from django.urls import path
from .views import *
urlpatterns = [
    
    
    path('settings/',settings , name="settings"),
    path('set/',set , name="set"),
     path('settings/update/<int:id>/',updated , name="profile_up"),
    path('settings/add-update/<int:id>/',addupdated , name="address_up"),
    path('settings/con-update/<int:id>/',conupdated , name="contact_up"),
    path('settings/con-pref/',conpref , name="pref"),
    path('settings/acc-deactivate/<int:id>/',deactivate_acc , name="deactivation"),
    path('settings/acc-deletion/<int:id>/',delete_account , name="deletion"),
    path('settings/suc',suc , name="success"),
    path('settings/sucess',success , name="suc"),
   
   
    
]

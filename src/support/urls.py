from django.urls import path
from .views import *
urlpatterns = [
    
    
   path('support/<int:id>/', support, name='support'),
    #path('supportt/',supportt2 , name="supportt"),
    
    
]

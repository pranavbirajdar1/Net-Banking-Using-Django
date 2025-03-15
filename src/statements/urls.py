from django.urls import path
from .views import *
urlpatterns = [

    
    #path('statement/',statement , name="statement"),
    path('statement/',StatementList.as_view() , name="statement"),
    
   
    
]

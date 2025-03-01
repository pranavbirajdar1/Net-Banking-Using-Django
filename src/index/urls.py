from django.urls import path
from .views import *
urlpatterns = [
    path('',index , name="home"),
    
    path('signup/', signup, name='signup'),  # URL
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    
    
]

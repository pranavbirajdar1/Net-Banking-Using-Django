from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index , name="home"),
    
    path('signup/', signup, name='signup'),  # URL
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    
    #Django password reset links
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
         name='password_reset'),
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
         name='password_reset_complete'),

]

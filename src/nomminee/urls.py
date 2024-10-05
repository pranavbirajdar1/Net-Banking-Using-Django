from django.urls import path
from . import views

urlpatterns = [
    path('nominees/', views.nominee, name='nominee'),
    # Add other paths as needed
]
from django.urls import path
from .views import *

urlpatterns = [
    path('nominees/<int:id>', nominee, name='nominee'),
    path('nominees/delnom/<int:id>', delnom, name='delnom'),
    path('nominees/editnom/<int:id>', editnom, name='editnom'),
    path('nominees/addnom/<int:id>', addnom, name='addnom'),
]
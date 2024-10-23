from django.shortcuts import render
from index.models import *
from index.models import *

def userdashboard(request):
    
    return render(request, 'userdashboard.html',context= { 'user': request.user})




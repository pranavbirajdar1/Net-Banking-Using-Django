from django.shortcuts import render
from index.models import *
from index.models import *
from django.contrib.auth.decorators import login_required


@login_required
def userdashboard(request):
    
    return render(request, 'userdashboard.html',context= { 'user': request.user})




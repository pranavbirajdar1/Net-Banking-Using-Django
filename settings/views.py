from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def userDeletion(user_id):
    user = User.objects.get(id)
    

def settings(request):
    
    return render(request, 'settings.html')


def deleteacc(request):
    
    return render(request, 'del.html')


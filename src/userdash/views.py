from django.shortcuts import render,redirect,get_object_or_404
from index.models import *
from index.models import *
from django.contrib.auth.decorators import login_required


@login_required
def userdashboard(request):
    
    return render(request, 'userdashboard.html',context= { 'user': request.user})



from .models import NewsLetter
@login_required
def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        NewsLetter.objects.create(email=email)
    return redirect(request.META.get('HTTP_REFERER'))
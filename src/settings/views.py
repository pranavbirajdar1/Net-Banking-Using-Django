from django.shortcuts import render,get_object_or_404
from index.models import *
# Create your views here.


def settings(request):
    user = request.user
    per = get_object_or_404(CustomerPersonalInfo ,user=user)
    add = get_object_or_404(AddressInfo ,user=user)
    con = get_object_or_404(Contact ,user=user)
    context = {
    'p':per,
    'a':add ,
    'c':con
    }
    return render(request, 'settings.html',context)




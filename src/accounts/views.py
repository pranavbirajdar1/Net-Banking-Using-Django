from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def accounts(request):
    return render(request, 'accounts.html')















from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def fundtransfer(request):
    user = request.user
    if request.method == 'POST':
        account_type = request.POST.get('fromAccount')
        toAccount = request.POST.get('toAccount')
        amount = request.POST.get('amount')
        date = request.POST.get('transferDate')
        note = request.POST.get('notes')
         
        
        
        
    return render(request, 'fundtransfer.html')


from django.shortcuts import render,redirect,get_object_or_404
from fundtransfer.models import Accbalance , Statement
from django.contrib.auth.decorators import login_required


@login_required
def userdashboard(request):
    try:
        balance = Accbalance.objects.get(user=request.user)
    except Accbalance.DoesNotExist:
        balance = 0.00
        message = "No balance record found for your account. Please contact support or try again later."
    else:
        message = None  # If balance exists, no message

    transaction_count = Statement.objects.filter(user = request.user).count()
    credit_count = Statement.objects.filter(user = request.user , transaction_type = 'Credit').count()
    debit_count = Statement.objects.filter(user = request.user , transaction_type = 'Debit').count()

    context = {
        'user': request.user,
        'user_id': request.user.id,
        'balance': balance,
        'message': message , # Pass the message to the template
        'tc' : transaction_count ,
        'cc' : credit_count ,
        'dc' : debit_count ,
    }
    
    return render(request, 'userdashboard.html', context)


from .models import NewsLetter
@login_required
def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email','').strip()
        NewsLetter.objects.create(email=email)
    return redirect(request.META.get('HTTP_REFERER'))
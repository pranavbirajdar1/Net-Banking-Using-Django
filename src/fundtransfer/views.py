from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import  Transaction
from decimal import Decimal,InvalidOperation
import logging
# Create your views here.


@login_required
def fundtransfer(request):
    user = request.user
    if request.method == 'POST':
        receiver_usernames = request.POST.get('username')
        amounts = request.POST.get('amount')
        sender = request.user
        receiver_username = receiver_usernames.strip()
        if not amounts:
            messages.error(request, 'Please enter the Amount')
            return redirect('fundtransfer')
        try:
            receiver = User.objects.get(username__iexact=receiver_username)
        except User.DoesNotExist:
            messages.error(request, 'Receiver not found , checkname')
            return redirect('fundtransfer')
       
        #Validate the amt must be +ve Number
        try:
            amounts = Decimal(amounts)
            if amounts <= 0:
                messages.error(request, 'Amount must be greater than zero')
                return redirect('fundtransfer')
            
        except ValueError:
            messages.error(request, 'Invalid amount. Please enter valid Number.')
            return redirect('fundtransfer')
        
        
        except InvalidOperation:
            # This will catch invalid inputs (like non-numeric or malformed input)
            messages.error(request, 'Invalid amount format. Please enter a valid number')
            return redirect('fundtransfer')
        
        
        #check if sender has sufficient balance
        sender_balance = sender.account_balance.current_balance
        if sender_balance < amounts:
            messages.error(request, 'Insufficient balance for this transaction')
            return redirect('fundtransfer')
        
        
        # Perform the Transfer
        try:
            Transaction.transfer_funds(sender=sender,receiver=receiver,amount=amounts)
            messages.success(request, f'Successfully Transferred {amounts} to {receiver_username.username}.')
            return redirect('fundtransfer')
            
        except Exception as e:
            messages.error(request, f'Error occurred during transfer {str(e)}')
            return redirect('fundtransfer')
    # Fetch users excluding logged in user  (for dropdown option in template)
    users = User.objects.exclude(username=user.username).exclude(is_superuser=True)
    context = {
        'users': users,
    }
    return render(request, 'fundtransfer.html',context=context)


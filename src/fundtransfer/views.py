from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import  Transaction , TransactionLog
from index.models import Contact
from decimal import Decimal,InvalidOperation
import logging
from django.core.mail import send_mail
# Create your views here.


@login_required
def fundtransfer(request):
    senderEmail = Contact.objects.get(user=request.user)
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
            messages.success(request, f'Successfully Transferred {amounts} to {receiver.username}.')
            senderforlog =sender.username
            receiverforlog = receiver.username
            TransactionLog.objects.create(status='Successful',sender =senderforlog , receiver = receiverforlog)
            send_sucessful_email(senderEmail,receiver_username,amounts)
            return redirect('fundtransfer')
            
        except Exception as e:
            messages.error(request, f'Error occurred during transfer {str(e)}')
            senderforlog =sender.username
            receiverforlog = receiver.username
            TransactionLog.objects.create(status='Failed',sender =senderforlog , receiver = receiverforlog)
            send_failure_email(senderEmail,receiver_username,amounts)
            return redirect('fundtransfer')
    # Fetch users excluding logged in user  (for dropdown option in template)
    users = User.objects.exclude(username=user.username).exclude(is_superuser=True)
    context = {
        'users': users,
    }
    return render(request, 'fundtransfer.html',context=context)



def send_failure_email(sender_email,receiver_username,amount):
    #send email to sender for failed transaction
    subject = f'Fund Transfer Failed'
    messsage = (
        f'Hello {sender_email},\n\n'
        f'We have emailed inform you that Your Transfer of amount {amount} to {receiver_username} has failed due to technical errors,'
        f'Please try again later or contact Support if the issue persists.\n\n'
        f'Best regards,\n\n Your Banking Team'
    )
    send_mail(
        subject=subject,
        message=messsage,
        from_email='your_email@gmail.com',
        recipient_list=[sender_email],
        fail_silently=False,
    )

    
def send_sucessful_email(sender_email,receiver_username,amount):
    #send email to sender for failed transaction
    subject = f'Fund Transfer Sucessful'
    messsage = (
        f'Hello {sender_email},\n\n'
        f'We have emailed inform you that Your Transfer of amount {amount} to {receiver_username} has been Sucessful,'
        f'Best regards,\n\n Your Banking Team'
    )
    send_mail(
        subject=subject,
        message=messsage,
        from_email='your_email@gmail.com',
        recipient_list=[sender_email],
        fail_silently=False,
    )
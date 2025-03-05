from celery import shared_task
from django.db import transaction
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)
@shared_task(bind=True,max_retries=3,default_retry_delay=10)
def fund_transferrs(self,sender_id,receiver_id,amount):
    try:
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        
        if sender.account_balance.current_balance < amount :
            raise ValidationError('Insufficient Client Balance For Transfer')
        with transaction.atomic():
            sender_acc = sender.account_balance
            receiver_acc = receiver.account_balance
             
            sender_balance_before = sender_acc.current_balance
            receiver_balance_before = receiver_acc.current_balance
            
            sender_acc.current_balance -= amount
            receiver_acc.current_balance += amount
            
            sender_acc.save(update_fields=['current_balance'])
            receiver_acc.save(update_fields=['current_balance'])
            
            
            #Transaction creation
            tx = Transaction.objects.create(
                sender=sender,
                receiver=receiver,
                amount=amount,
            )
            statements = [
                Statement(
                    user =sender,
                    transaction = tx,
                    transaction_type = 'Debit',
                    amount = amount,
                    balance_before = sender_balance_before,
                    balance_after = sender_acc.current_balance
                ),
                Statement(
                    user =receiver,
                    transaction = tx,
                    transaction_type = 'Credit',
                    amount = amount,
                    balance_before = receiver_balance_before,
                    balance_after = receiver_acc.current_balance,
                )
            ]
            #bulk creation
            Statement.objects.bulk_create(statements)
            logger.info(f'Successful Transfer : {amount} from {sender.username} to {receiver.username}')
            senderforlog =sender.username
            receiverforlog = receiver.username
            TransactionLog.objects.bulk_create(status='Successful',sender =senderforlog , receiver = receiverforlog)
            return f'Transfer of {amount} from {sender.username} to {receiver.username} completed'
        
    
    except ValidationError as e:
        logger.error(f'Failed Transfer : {amount} from {sender.username} to {receiver.username}')
        send_failure_email(sender.email,receiver.username,amount)
        TransactionLog.objects.bulk_create(status='Failed',sender =senderforlog , receiver = receiverforlog)
        raise self.retry(exe = e)
    
    
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
        
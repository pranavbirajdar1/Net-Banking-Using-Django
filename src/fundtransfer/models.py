from django.db import models
from model_utils import FieldTracker
from django.contrib.auth.models import User
from django.db import transaction
from statements.models import Statement
from django.core.exceptions import ValidationError
from django.utils.timezone import now


# Create your models here.
class Accbalance(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING,related_name='account_balance',related_query_name='acc_bal')
    current_balance = models.DecimalField(max_digits=12,decimal_places=2)
    tracker = FieldTracker()
    def __str__(self):
        return f'{self.user.username} : {self.current_balance}'
    
        
        
class Transaction(models.Model):
    sender = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='sent_transactions')
    receiver = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='received_transactions')
    sender_balance = models.ForeignKey(Accbalance , on_delete=models.DO_NOTHING , related_name='transactons_as_sender')
    receiver_balance = models.ForeignKey(Accbalance , on_delete=models.DO_NOTHING , related_name='transactons_as_receiver')
    amount = models.DecimalField(max_digits=12 , decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Transaction of {self.amount} from {self.sender.username} {self.receiver.username} on {self.timestamp}'
    
    
    @classmethod
    def transfer_funds(cls,sender,receiver,amount):
        ''' Handles the fund transfer betn users with
            balance updates and transaction creation'''
            
        if sender.account_balance.current_balance < amount :
            raise ValidationError('Insufficient balance for Transfer')
        with transaction.atomic():
            sender_acc = sender.account_balance
            receiver_acc = receiver.account_balance
            
            sender_acc.current_balance -= amount 
            receiver_acc.current_balance += amount 
            
            sender_acc.save(update_fields = ['current_balance'])
            receiver_acc.save(update_fields = ['current_balance'])
            
            tx = cls.objects.create(
                sender = sender ,
                receiver = receiver ,
                sender_balance = sender_acc ,
                receiver_balance = receiver_acc ,
                amount = amount ,
            )
            Statement.objects.create
            (
                user = sender ,
                transaction = tx ,
                transaction_type = 'Debit',
                amount = amount ,
                balance_before = sender_acc.current_balance += amount ,
                balance_after = sender_acc.current_balance 
            )
            Statement.objects.create
            (
                user = receiver ,
                transaction = tx ,
                transaction_type = 'Credit',
                amount = amount ,
                balance_before = receiver_acc.current_balance -= amount ,
                balance_after = receiver_acc.current_balance 
            )
            return tx
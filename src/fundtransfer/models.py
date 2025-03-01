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
    def transfer_funds(cls, sender, receiver, amount):
        '''Handles the fund transfer between users with
        balance updates and transaction creation'''

        if sender.account_balance.current_balance < amount:
            raise ValidationError('Insufficient balance for Transfer')

        with transaction.atomic():
            sender_acc = sender.account_balance
            receiver_acc = receiver.account_balance

            # Capture balance before the transaction (before the update)
            sender_balance_before = sender_acc.current_balance
            receiver_balance_before = receiver_acc.current_balance

            # Perform the transfer (updating the balances)
            sender_acc.current_balance -= amount  # Subtract from sender's balance
            receiver_acc.current_balance += amount  # Add to receiver's balance

            # Save the updated balances to the database
            sender_acc.save(update_fields=['current_balance'])
            receiver_acc.save(update_fields=['current_balance'])

            # Capture balance after the transaction (after the update)
            sender_balance_after = sender_acc.current_balance
            receiver_balance_after = receiver_acc.current_balance

            # Create the transaction record
            tx = cls.objects.create(
                sender=sender,
                receiver=receiver,
                sender_balance=sender_acc,
                receiver_balance=receiver_acc,
                amount=amount,
            )

            # Create Statement records for both sender and receiver using captured balances
            sender_statement = {
                'user': sender,
                'transaction': tx,
                'transaction_type': 'Debit',
                'amount': amount,
                'balance_before': sender_balance_before,
                'balance_after': sender_balance_after,
            }

            receiver_statement = {
                'user': receiver,
                'transaction': tx,
                'transaction_type': 'Credit',
                'amount': amount,
                'balance_before': receiver_balance_before,
                'balance_after': receiver_balance_after,
            }

            # Now pass the statement data and create the records
            Statement.objects.create(**sender_statement)
            Statement.objects.create(**receiver_statement)

            return tx
from django.db import models
from django.contrib.auth.models import User
from fundtransfer.models import Transaction
from model_utils import FieldTracker
# Create your models here.

class Statement(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='statements')
    transaction =models.ForeignKey(Transaction, on_delete=models.DO_NOTHING,related_name='transactions')
    transaction_type = models. CharField(max_length=10, choices=[('Credit','Credit'),('Debit','Debit')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance_before = models.DecimalField(max_digits=10, decimal_places=2)
    balance_after = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    tracker = FieldTracker()
    def __str__(self):
        return f'{self.transaction_type} of {self.amount} on {self.timestamp}.'
    
    
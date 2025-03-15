from django.test import TestCase
from django.db.models import Sum
from fundtransfer.models import Statement


user = request.user  # or any User object

total = Statement.objects.filter(user=user).aggregate(total_sum=Sum('amount'))
print(total['total_sum'])  # Output: Decimal('1234.56') or 


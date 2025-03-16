from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def statement(request):
    return render(request, 'statement.html')







from django.utils.dateparse import parse_date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from fundtransfer.models import Statement
from django.utils.timezone import make_aware, get_default_timezone
from datetime import datetime, time, timezone

class StatementList(LoginRequiredMixin, ListView):
    model = Statement
    template_name = "statement.html"
    context_object_name = "data"
    paginate_by = 10  

    def get_queryset(self):
        queryset = Statement.objects.filter(user=self.request.user)
        print(f"DEBUG - All Statements for User: {queryset}")

        # Get values from GET request
        transaction_type = self.request.GET.get("transactionType", "").strip().lower()  # Normalize input
        date_from = self.request.GET.get("fromDate", "")
        date_to = self.request.GET.get("toDate", "")

        # Convert date strings to timezone-aware UTC datetime
        if date_from:
            date_from = parse_date(date_from)
            if date_from:
                date_from = make_aware(datetime.combine(date_from, time.min), get_default_timezone()).astimezone(timezone.utc)

        if date_to:
            date_to = parse_date(date_to)
            if date_to:
                date_to = make_aware(datetime.combine(date_to, time.max), get_default_timezone()).astimezone(timezone.utc)

        print(f"DEBUG - Converted Dates to UTC: Date From: {date_from}, Date To: {date_to}")

        # Debug available transaction types in DB
        db_transaction_types = Statement.objects.values_list('transaction_type', flat=True).distinct()
        print(f"DEBUG - Available Transaction Types in DB: {list(db_transaction_types)}")
        print(f"DEBUG - Transaction Type from Request: {transaction_type}")

        # Apply filters
        if transaction_type in ["debit", "credit"]:  # Ensure it matches stored values
            queryset = queryset.filter(transaction_type__iexact=transaction_type)  # Case-insensitive match

        if date_from and date_to:
            queryset = queryset.filter(timestamp__range=[date_from, date_to])
        elif date_from:
            queryset = queryset.filter(timestamp__gte=date_from)
        elif date_to:
            queryset = queryset.filter(timestamp__lte=date_to)

        print(f"DEBUG - Final Filtered Queryset: {queryset}")
        print(f"DEBUG - SQL Query: {queryset.query}")

        return queryset






# from weasyprint import HTML
# from django.utils import timezone
# from datetime import datetime
# from index.models import *
# from fundtransfer.models import Statement
# from django.template.loader import get_template
# from io import BytesIO
# from django.http import HttpResponse
# from django.db.models import Sum, Q
# from io import BytesIO

# def pdf_generate(request):
#     user = request.user
#     cp = CustomerPersonalInfo.objects.get(user=user)
#     con = Contact.objects.get(user = user)
#     statement = Statement.objects.filter(user=user).order_by('-timezone')
#     bank = AccountDetails.objects.get(user = user)
#     time = timezone.now()
#     # Aggregate totals
#     totals = statements.aggregate(
#         total_debit=Sum('amount', filter=Q(transaction_type='debit')),
#         total_credit=Sum('amount', filter=Q(transaction_type='credit'))
#     )

#     # Default to 0 if None
#     total_debit = totals['total_debit'] or 0
#     total_credit = totals['total_credit'] or 0

#     context = {
#         'first':cp.first_name , 
#         'middle':cp.middle_name , 
#         'last':cp.last_name , 
#         'aodt':cp.account_opening_date_time , 
#         'type': cp.account_type , 
#         'con' : con , 
#         'branch_name' : bank.bankbranch , 
#         'account_number' : bank.account_number ,
#         'ifsc' : bank.ifsc ,
#         'generated_time' : time ,
#         'statements' : statement ,
#         'totalcredit' : total_credit ,
#         'totaldebit' : total_debit ,
#     }
#     template = get_template('pdf_template.html')
#     html_string = template.render(context)
#     pdf_file = HTML(string=html_string).write_pdf()

#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="bank_statement.pdf"'
#     return response


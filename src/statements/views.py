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
from django.contrib import admin
from .models import Transaction, Accbalance, Statement ,TransactionLog

# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ('sender', 'receiver', 'amount', 'timestamp')
#     search_fields = ('sender__username', 'receiver__username')
#     list_filter = ('timestamp',)
#     ordering = ('-timestamp',)
#     # Enabling inline editing of specific fields (if needed)
#     # fields = ('sender', 'receiver', 'amount', 'timestamp')  # Example for specific fields to show on form
#     # You can also enable editing of all fields, by leaving it to the default behavior
    
#     # Enable deleting records from the admin interface (default behavior)
#     actions = ['delete_selected']

# class AccbalanceAdmin(admin.ModelAdmin):
#     list_display = ('user', 'current_balance')
#     search_fields = ('user__username',)
#     ordering = ('-current_balance',)
#     # Enable deleting records from the admin interface (default behavior)
#     actions = ['delete_selected']

# class StatementAdmin(admin.ModelAdmin):
#     list_display = ('user', 'transaction', 'transaction_type', 'amount', 'timestamp')
#     search_fields = ('user__username', 'transaction__sender__username', 'transaction__receiver__username')
#     list_filter = ('transaction_type', 'timestamp')
#     ordering = ('-timestamp',)
#     # Enable deleting records from the admin interface (default behavior)
#     actions = ['delete_selected']



# # Registering models with admin.site.register() directly

# admin.site.register(Transaction, TransactionAdmin)
# admin.site.register(Accbalance, AccbalanceAdmin)
# admin.site.register(Statement, StatementAdmin)
admin.site.register(TransactionLog)

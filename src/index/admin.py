from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CustomerPersonalInfo)
@admin.register(Contact)
@admin.register(AddressInfo)
@admin.register(AccountDetails)
@admin.register(SecurityQuestion)
@admin.register(IsAuthenticated)
class CustomerPersonalInfoAdmin(admin.ModelAdmin):
    
    
    pass

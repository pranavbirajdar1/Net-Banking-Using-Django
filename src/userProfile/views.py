from django.shortcuts import render, get_object_or_404
from index.models import CustomerPersonalInfo, Contact, AddressInfo

def profile(request):
    user = request.user
    
    try:
        cust = CustomerPersonalInfo.objects.get(user=user) 
    except CustomerPersonalInfo.DoesNotExist:
        cust = None

    try:
        contact = Contact.objects.get(user=user)
    except Contact.DoesNotExist:
        contact = None

    try:
        add = AddressInfo.objects.get(user=user)
    except AddressInfo.DoesNotExist:
        add = None

    context = {
        'user': user,
        'c': cust,
        'con': contact,
        'add': add,
    }
    
    return render(request, 'profile.html', context)

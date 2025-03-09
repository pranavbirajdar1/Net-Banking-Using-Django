from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.contrib import messages
from index.models import CustomerPersonalInfo, Contact, AddressInfo, User
from userProfile.models import ContactPreference
from .models import *
from django.contrib.auth.decorators import login_required
# Profile view (unchanged)


@login_required
def settings(request):
    user = request.user

    # Fetch existing preferences
    email_prefs, _ = EmailPreferences.objects.get_or_create(user=user)
    push_prefs, _ = PushNotificationPreferences.objects.get_or_create(user=user)

    # Handle SMS Alert separately to avoid IntegrityError
    try:
        sms_prefs = SmsAlert.objects.get(user=user)
    except SmsAlert.DoesNotExist:
        sms_prefs = None  # No existing record

    if request.method == "POST":
        email_notifications = request.POST.get("emailNotif") == "on"  # Check if checkbox is checked
        sms_notifications = request.POST.get("smsNotif") == "on"
        push_notifications = request.POST.get("pushNotif") == "on"

        # Update email preferences
        email_prefs.notifications = email_notifications
        email_prefs.save()

        # Update SMS preferences (ensure no duplicate phone number)
        if sms_prefs:
            sms_prefs.status = sms_notifications
            sms_prefs.save()
        else:
            # If no record exists, create a new one with a phone number
            phone_number = request.POST.get("phone_number")  # Ensure this is coming from the form
            if phone_number:
                SmsAlert.objects.create(user=user, phone_number=phone_number, status=sms_notifications)

        # Update push notifications
        push_prefs.enabled = push_notifications
        push_prefs.save()

        messages.success(request, "Notification preferences updated successfully!")
        return redirect("suces")  # Redirect to the same page

    context = {
        "email_prefs": email_prefs,
        "sms_prefs": sms_prefs,
        "push_prefs": push_prefs,
    }
    return render(request, "settings.html", context)




def suc(request):
    return render(request, 'success.html')



def success(request):
    return render(request, 'success2.html')



def success2(request):
    return render(request, 'suc3.html')


# Update view
@login_required
def updated(request, id):
    user = request.user

    # Fetch related data in one go and handle exceptions using get_object_or_404 for better error management
    cust = get_object_or_404(CustomerPersonalInfo, user=user)


    context = {
        'user': user,
        'c': cust,
   
    }
    if request.method == 'POST':
        # Get all the fields, use '' as a default for missing data
        a = request.POST.get('firstname', '').strip()
        b = request.POST.get('middlename', '').strip()
        c = request.POST.get('lastname', '').strip()
        d = request.POST.get('gender', '').strip()
        e = request.POST.get('pan', '').strip()
        f = request.POST.get('addhar', '').strip()
        g = request.POST.get('occupation', '').strip()
        h = request.POST.get('email', '').strip()
        i = request.POST.get('phone', '').strip()
        hono = request.POST.get('hono', '').strip()
        me = request.POST.get('street', '').strip()
        k = request.POST.get('city', '').strip()
        l = request.POST.get('state', '').strip()
        m = request.POST.get('country', '').strip()
        n = request.POST.get('pincode', None)  # Handle pincode as optional
        o = request.POST.get('addresstype', '').strip()
        p = request.POST.get('username', '').strip()
        q = request.POST.get('annum', '').strip()
        r = request.POST.get('nationality', '').strip()
        s = request.POST.get('title', '').strip()
        t = request.POST.get('contacttype', '').strip()

        try:
            #with transaction.atomic():
                # Update CustomerPersonalInfo
                newpersonal = get_object_or_404(CustomerPersonalInfo, user_id=id)
                newpersonal.first_name = a
                newpersonal.middle_name = b
                newpersonal.last_name = c
                newpersonal.gender = d
                newpersonal.pan = e
                newpersonal.aadhaar = f
                newpersonal.title = s
                newpersonal.occupation = g
                newpersonal.nationality = r
                newpersonal.annual_income = q
                newpersonal.save()

                # Update User (Username)
                newname = get_object_or_404(User, id=id)
                newname.username = p
                newname.save()

                # Success message
                messages.success(request, 'Profile updated successfully!')
                return redirect('success')

        except Exception as e:
             # Handle any errors, rollback the transaction
                messages.error(request, f"An error occurred: {str(e)}")

    else:
    # If not a POST request, redirect back
        return render(request,'perinfo.html',context)



@login_required
def addupdated(request,id):
    user = request.user

    # Fetch related data in one go and handle exceptions using get_object_or_404 for better error management

    add = get_object_or_404(AddressInfo, user=user)

    context = {
        'user': user,
  
        'add': add,
    }

    
    if request.method == 'POST':
        hono = request.POST.get('hono', '').strip()
        me = request.POST.get('street', '').strip()
        k = request.POST.get('city', '').strip()
        l = request.POST.get('state', '').strip()
        m = request.POST.get('country', '').strip()
        n = request.POST.get('pincode', None)  # Handle pincode as optional
        o = request.POST.get('addresstype', '').strip()
        
        try:
            #with transaction.atomic():        
        # Update AddressInfo
                newadd = get_object_or_404(AddressInfo, user_id=id)
                newadd.address_type = o
                newadd.house_no = hono
                newadd.street = me
                newadd.city = k
                newadd.state = l
                newadd.country = m
                # Handle pincode validation - only save if it's not empty
                if n and n.isdigit():
                    newadd.pincode = int(n)
                else:
                    newadd.pincode = None  # Or some default value if pincode can be optional
                newadd.save()
                                # Success message
                                
                messages.success(request, 'Address updated successfully!')
                return redirect('success')
        
        except Exception as e:
             # Handle any errors, rollback the transaction
                messages.error(request, f"An error occurred: {str(e)}")
    
    
    else:
        return render(request,'addinfo.html',context)

@login_required
def conupdated(request,id):
    user = request.user

    # Fetch related data in one go and handle exceptions using get_object_or_404 for better error management
   
    contact = get_object_or_404(Contact, user=user)
    

    context = {
        'user': user,
        
        'con': contact,
        
    }


    if request.method == 'POST':
        t = request.POST.get('contacttype', '').strip()
        h = request.POST.get('contact_email', '').strip()
        i = request.POST.get('contact', '').strip()
        
        try:
            #with transaction.atomic():
            
            # Update Contact
                newcontact = get_object_or_404(Contact, user_id=id)
                newcontact.contact_type = t
                newcontact.contact = i
                newcontact.email = h
                newcontact.save()
            
                messages.success(request, 'Contact updated successfully!')
                return redirect('suc')
        
        except Exception as e:
             # Handle any errors, rollback the transaction
                messages.error(request, f"An error occurred: {str(e)}")
    
    
    else:    
        return render(request,'coninfo.html',context)
    
    
@login_required
def conpref(request):
    user = request.user  # Get the logged-in user
    
    # Fetch user preferences or create new if they don't exist
    preferences, created = ContactPreference.objects.get_or_create(user=user)

    if request.method == "POST":
        email_notifications = request.POST.get("emailNotifications")
        sms_notifications = request.POST.get("smsNotifications")

        # Update user preferences
        preferences.emailnotification = email_notifications
        preferences.smsnotification = sms_notifications
        preferences.save()

        messages.success(request, "Preferences updated successfully!")
        return redirect("suc")  # Redirect back to the same page

    return render(request, "conpref.html", {"preferences": preferences})



@login_required   
def deactivate_acc(request,id):
    if request.user.id == id:
        isactive = get_object_or_404(User, id=id)
        isactive.is_active = False
        isactive.save()
        messages.success(request, 'Account deactivated successfully!')
        return redirect('home')

from django.contrib.auth import logout
@login_required
def delete_account(request,id):
    if request.user.id == id:
        user = get_object_or_404(User, id=id)
        logout(request)
        user.delete()
        return redirect('home')
        
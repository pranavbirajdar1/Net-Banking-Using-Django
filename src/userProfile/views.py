from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.contrib import messages
from index.models import CustomerPersonalInfo, Contact, AddressInfo, User

# Profile view (unchanged)
def profile(request, id):
    user = request.user

    # Fetch related data in one go and handle exceptions using get_object_or_404 for better error management
    cust = get_object_or_404(CustomerPersonalInfo, user=user)
    contact = get_object_or_404(Contact, user=user)
    add = get_object_or_404(AddressInfo, user=user)

    context = {
        'user': user,
        'c': cust,
        'con': contact,
        'add': add,
    }

    return render(request, 'profile.html', context)


# Update view
def update(request, id):
    if request.method == 'POST':
        # Get all the fields, use '' as a default for missing data
        a = request.POST.get('firstname', '')
        b = request.POST.get('middlename', '')
        c = request.POST.get('lastname', '')
        d = request.POST.get('gender', '')
        e = request.POST.get('pan', '')
        f = request.POST.get('addhar', '')
        g = request.POST.get('occupation', '')
        h = request.POST.get('email', '')
        i = request.POST.get('phone', '')
        hono = request.POST.get('hono', '')
        me = request.POST.get('street', '')
        k = request.POST.get('city', '')
        l = request.POST.get('state', '')
        m = request.POST.get('country', '')
        n = request.POST.get('pincode', None)  # Handle pincode as optional
        o = request.POST.get('addresstype', '')
        p = request.POST.get('username', '')
        q = request.POST.get('annum', '')
        r = request.POST.get('nationality', '')
        s = request.POST.get('title', '')
        t = request.POST.get('contacttype', '')

        try:
            with transaction.atomic():
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

                # Update Contact
                newcontact = get_object_or_404(Contact, user_id=id)
                newcontact.contact_type = t
                newcontact.contact = i
                newcontact.email = h
                newcontact.save()

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

                # Update User (Username)
                newname = get_object_or_404(User, id=id)
                newname.username = p
                newname.save()

                # Success message
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile_update', id=id)

        except Exception as e:
             # Handle any errors, rollback the transaction
                messages.error(request, f"An error occurred: {str(e)}")

    # If not a POST request, redirect back
    return redirect('profile_update', id=id)
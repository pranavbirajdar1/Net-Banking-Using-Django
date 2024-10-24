from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.contrib import messages
from index.models import CustomerPersonalInfo, Contact, AddressInfo, User

def profile(request,id):
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
    if request.method=='POST':
        a = request.POST['firstname']
        b = request.POST['middlename']
        c = request.POST['lastname']
        d= request.POST['gender']
        e = request.POST['pan']
        f = request.POST['addhar']
        g = request.POST['occupation']
        h = request.POST['email']
        i = request.POST['phone']
        j = request.POST['hono']
        me = request.POST['street']
        k = request.POST['city']
        l = request.POST['state']
        m = request.POST['country']
        n = request.POST['pincode']
        o = request.POST['addresstype']
        p = request.POST['username']
        q = request.POST['annum']
        r = request.POST['nationality']
        s = request.POST['title']
        t = request.POST['contacttype']
        try:
            with transaction.atomic():
                # Update CustomerPersonalInfo
                newpersonal = CustomerPersonalInfo.objects.get(id=id)
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
                newcontact = Contact.objects.get(id=id)
                newcontact.contact_type = t
                newcontact.contact = i
                newcontact.email = h
                newcontact.save()

                # Update AddressInfo
                newadd = AddressInfo.objects.get(id=id)
                newadd.address_type = o
                newadd.house_no = j
                newadd.street = me
                newadd.city = k
                newadd.state = l
                newadd.country = m
                newadd.pincode = n
                newadd.save()

                # Update User (Username)
                newname = User.objects.get(id=id)
                newname.username = p
                newname.save()

                # Success message
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile', id=user.id)

        except Exception as e:
            # In case of any error, rollback and show an error message
            messages.error(request, f"An error occurred: {str(e)}")


    return render(request, 'profile.html', context)

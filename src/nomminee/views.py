from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Nominee

# Create your views here.

@login_required
def nominee(request, id):
    try:
        nom = Nominee.objects.get(user_id=id)
        context = {'nominee': nom}
        if request.method == 'POST':
            pass
        return render(request, 'nominee.html', context)
    except Nominee.DoesNotExist:
        return render(request, 'new2.html')
    

@login_required
def addnom(request ,id):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name','').strip()
        rel = request.POST.get('relationship','').strip()
        con = request.POST.get('contact','')
        if con.isdigit() and len(con) == 10:
            nominee =Nominee.objects.create(
                name=name,
                relation=rel,
                contact=con,
                 user=user,
            )
            messages.success(request,'Congrats Nominee Added Successfully !!')
            return redirect('nominee',id=id)
    return render(request,'new2.html')



@login_required
def delnom(request, id ):
    nominee = Nominee.objects.get( user_id = id).delete()
    #nominee.save()
    return redirect('nominee' , id = id )
    




@login_required
def editnom(request ,id):
    user = request.user
    nominee = Nominee.objects.get(user_id =id)
    context = {
        'nominee':nominee
    }
    if request.method == 'POST':
        name = request.POST.get('name','').strip()
        rel = request.POST.get('relation','').strip()
        con = request.POST.get('contact','')

        updated = False  # Track if anything changed

        if name and name != nominee.name:
            nominee.name = name
            updated = True

        if rel :
            nominee.relation = rel
            updated = True

        if con.isdigit() and len(con) == 10 and con != nominee.contact:
            nominee.contact = con
            updated = True

        if updated:
            nominee.save()
            messages.success(request, "Nominee updated successfully.")
            return redirect("nominee", id=id)
        else:
            messages.info(request, 'Welcome, Here You can Update Your Nominee Details.') 


    return render(request,'nomminee-Management.html',context=context)
    



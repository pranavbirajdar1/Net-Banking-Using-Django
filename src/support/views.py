'''
#add emaill services

from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def support(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail('Support Request', 'Name: ' + name + '\nEmail: ' +
                  email + '\nMessage: ' + message, 'your-email@gmail.com',
                  ['your-email@gmail.com'], fail_silently=False)
        return render(request, 'support.html', {'message': 'Email sent successfully.'})
    
    return render(request, 'support.html')

'''


from django.shortcuts import render,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Support
from django.contrib.auth.decorators import login_required
from index.models import Contact,CustomerPersonalInfo



@login_required
def support(request):
    user = request.user
    name=get_object_or_404(CustomerPersonalInfo,user=user)
    email=get_object_or_404(Contact,user=user)
    info = {
    'name': name,
    'email': email
          }
    
    # Replace this with the actual registered email logic
    registered_email = settings.REGISTERED_EMAIL  # Make sure to set this in your settings.py

    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
       
        
        # Create email body
        email_body = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Subject: {subject}\n"
            f"Message:\n{message}"
        )
        
        try:
            send_mail(
                subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,  # Your configured email
                [registered_email],  # Send to the registered email
                fail_silently=False
            )
            return render(request, 'support2.html', {'message': 'Email sent successfully.'})
        except Exception as e:
            return render(request, 'support2.html', {'message': f'Error sending email: {str(e)}'})

    return render(request, 'support.html' ,info)


#@login_required
def supportt2(request):
   user = request.user
   name=get_object_or_404(CustomerPersonalInfo,user=user)
   email=get_object_or_404(Contact,user=user)
   info = {
    'name': name,
    'email': email
          }
   if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       
   
   return render(request, 'support2.html',info)

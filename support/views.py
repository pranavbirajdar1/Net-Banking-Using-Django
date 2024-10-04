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


from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Support

def support(request):
    # Replace this with the actual registered email logic
    registered_email = settings.REGISTERED_EMAIL  # Make sure to set this in your settings.py

    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        new_support = Support(name = name ,
                              email = email,
                              subject = subject ,
                              message = message)
        new_support.save()
       
        
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

    return render(request, 'support2.html')


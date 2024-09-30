from django.shortcuts import render

# Create your views here.

def support(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail('Support Request', 'Name: ' + name + '\nEmail: ' +
                  email + '\nMessage: ' + message, 'your-email@gmail.com',
                  ['your-email@gmail.com'], fail_silently=False)
        return render(request, 'support.html', {'message': 'Email sent successfully.'})
    
    return render(request, 'support.html')



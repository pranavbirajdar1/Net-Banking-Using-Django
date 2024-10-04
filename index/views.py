from django.shortcuts import render, redirect
from django.contrib.auth import login ,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomerPersonalInfoForm, AddressInfoForm, ContactForm, SecurityQuestionForm
from django.contrib.auth.forms import AuthenticationForm
def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        personal_info_form = CustomerPersonalInfoForm(request.POST)
        address_info_form = AddressInfoForm(request.POST)
        contact_form = ContactForm(request.POST)
        security_question_form = SecurityQuestionForm(request.POST)

        if (user_form.is_valid() and personal_info_form.is_valid() and 
                address_info_form.is_valid() and contact_form.is_valid() and 
                security_question_form.is_valid()):
            # Create the user
            user = user_form.save()
            user.refresh_from_db()  # Load the user instance to update it
            personal_info = personal_info_form.save(commit=False)
            personal_info.user = user
            personal_info.save()

            address_info = address_info_form.save(commit=False)
            address_info.user = user
            address_info.save()

            contact = contact_form.save(commit=False)
            contact.user = user
            contact.save()

            security_question = security_question_form.save(commit=False)
            security_question.user = user
            security_question.save()

            messages.success(request, 'Account created successfully!')
            login(request, user)  # Log the user in after signup
            return redirect('login')  # Redirect to home or another page as needed
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        user_form = UserCreationForm()
        personal_info_form = CustomerPersonalInfoForm()
        address_info_form = AddressInfoForm()
        contact_form = ContactForm()
        security_question_form = SecurityQuestionForm()

    context = {
        'user_form': user_form,
        'personal_info_form': personal_info_form,
        'address_info_form': address_info_form,
        'contact_form': contact_form,
        'security_question_form': security_question_form,
    }
    
    return render(request, 'signup.html', context)

   

def index(request):
    return render(request, 'index.html')

def acknowledge(request):
    return render(request, 'acknowledge.html')


   
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully.')
                return redirect('userdashboard')  # Redirect to the desired page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    #messages.success(request, 'You have logged out successfully.')
    return redirect('home')  # Redirect to login page or another page as needed
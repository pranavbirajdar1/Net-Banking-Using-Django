from django.db import models
from django.contrib.auth.models import User
from model_utils import FieldTracker


# Gender choices
GENDERC = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

# Occupation choices
OCCUPATION_CHOICES = [
    ('Student', 'Student'),
    ('Salaried', 'Salaried'),
    ('Non-Salaried', 'Non-Salaried'),
    ('Housewife', 'Housewife'),
    ('Other', 'Other'),
]

# Account Type choices
ACCOUNT_TYPE_CHOICES = [
    ('Saving BANK ACCOUNT', 'Saving BANK ACCOUNT'),
    ('Current BANK ACCOUNT', 'Current BANK ACCOUNT'),
]

# Security Question choices
SECURITY_QUESTIONS = [
    ('mother_maiden_name', 'What is your mother\'s maiden name?'),
    ('first_pet', 'What was the name of your first pet?'),
    # Add more questions here as needed
]

class CustomerPersonalInfo(models.Model):
    index = models.BigAutoField(db_index=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Personal Details', default=1)
    title_choices = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
    ]
    title = models.CharField(max_length=3, choices=title_choices, verbose_name="Title")
    first_name = models.CharField(max_length=10, verbose_name="First Name")
    middle_name = models.CharField(max_length=10, verbose_name="Middle Name", blank=True)
    last_name = models.CharField(max_length=10, verbose_name="Last Name")
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=6, choices=GENDERC, verbose_name="Gender")
    pan = models.CharField(max_length=15, unique=True, verbose_name="PAN")
    aadhaar = models.CharField(max_length=12, unique=True, verbose_name="Aadhaar Card")
    occupation = models.CharField(max_length=13, choices=OCCUPATION_CHOICES, verbose_name="Occupation")
    annual_income = models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Annual Income")
    nationality = models.CharField(max_length=19, verbose_name="Nationality")
    account_opening_date_time = models.DateTimeField(auto_now_add=True)
    account_type = models.CharField(max_length=22, choices=ACCOUNT_TYPE_CHOICES, verbose_name="Account Type")

    tracker = FieldTracker()  # Tracks all fields on the model

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Capitalize names and format pan before saving
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize() if self.middle_name else ''
        self.last_name = self.last_name.capitalize()
        self.pan = self.pan.upper()
        self.aadhaar = ''.join(filter(str.isdigit, self.aadhaar))
        super(CustomerPersonalInfo, self).save(*args, **kwargs)
        
        
class AddressInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='Address Info', on_delete=models.CASCADE, default=1)
    address_type = models.CharField(max_length=20, verbose_name='Address Type')
    house_no = models.CharField(max_length=5, verbose_name="House No")
    street = models.CharField(max_length=20, verbose_name="Street")
    city = models.CharField(max_length=20, verbose_name="City")
    state = models.CharField(max_length=20, verbose_name="State")
    country = models.CharField(max_length=20, verbose_name="Country")
    pincode = models.IntegerField(verbose_name="Pincode")
    tracker = FieldTracker()  # Tracks all fields on the model


    def __str__(self):
        return f"Address: {self.house_no}, {self.city}"
    
    def save(self, *args, **kwargs):
        # Capitalize names before saving
        self.street = self.street.capitalize()
        self.city = self.city.capitalize()
        self.state = self.state.capitalize()
        self.country = self.country.capitalize()
        super(AddressInfo, self).save(*args, **kwargs)

    

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='Contact', on_delete=models.CASCADE, default=1)
    contact_type = models.CharField(max_length=20, verbose_name='Contact Type')
    contact = models.BigIntegerField(verbose_name='Contact')
    email = models.EmailField(verbose_name="Email")
    tracker = FieldTracker()  # Tracks all fields on the model

    def __str__(self):
        return f"Contact: {self.contact} ({self.email})"

class SecurityQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, verbose_name='Security Question', on_delete=models.CASCADE, default=1)
    question = models.CharField(max_length=50, choices=SECURITY_QUESTIONS, verbose_name='Security Question')
    answer = models.CharField(max_length=100, verbose_name='Answer')
    tracker = FieldTracker()  # Tracks all fields on the model

    def __str__(self):
        return f"Security Question for {self.user.first_name} {self.user.last_name}"

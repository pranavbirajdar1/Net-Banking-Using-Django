from django import forms
from .models import CustomerPersonalInfo, AddressInfo, Contact, SecurityQuestion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

class CustomerPersonalInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerPersonalInfo
        fields = [
            'title', 'first_name', 'middle_name', 'last_name', 'dob',
            'gender', 'pan', 'aadhaar', 'occupation', 'annual_income',
            'nationality', 'account_type'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'annual_income': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'pan': forms.TextInput(attrs={'maxlength': 15, 'class': 'form-control', 'placeholder': 'ABCDE1234F'}),
            'aadhaar': forms.TextInput(attrs={'maxlength': 12, 'class': 'form-control', 'placeholder': '1234-5678-9012'}),
        }

    def clean_aadhaar(self):
        aadhaar = self.cleaned_data.get('aadhaar')
        if len(aadhaar) != 12:
            raise forms.ValidationError("Aadhaar number must be 12 digits long.")
        return aadhaar

    def __init__(self, *args, **kwargs):
        super(CustomerPersonalInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-4 mb-0'),
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('middle_name', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                Column('dob', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('gender', css_class='form-group col-md-4 mb-0'),
                Column('pan', css_class='form-group col-md-4 mb-0'),
                Column('aadhaar', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('occupation', css_class='form-group col-md-6 mb-0'),
                Column('annual_income', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('nationality', css_class='form-group col-md-6 mb-0'),
                Column('account_type', css_class='form-group col-md-6 mb-0')
            ),
            Submit('submit', 'Submit')
        )


class AddressInfoForm(forms.ModelForm):
    class Meta:
        model = AddressInfo
        fields = [
            'address_type', 'house_no', 'street', 'city', 'state', 
            'country', 'pincode'
        ]
        widgets = {
            'pincode': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'house_no': forms.TextInput(attrs={'maxlength': 5, 'class': 'form-control'}),
            'street': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'maxlength': 20, 'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_type', 'contact', 'email']
        widgets = {
            'contact': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'maxlength': 254, 'class': 'form-control', 'placeholder': 'you@example.com'}),
        }

class SecurityQuestionForm(forms.ModelForm):
    class Meta:
        model = SecurityQuestion
        fields = ['question', 'answer']
        widgets = {
            'answer': forms.TextInput(attrs={'maxlength': 100, 'class': 'form-control'}),
        }

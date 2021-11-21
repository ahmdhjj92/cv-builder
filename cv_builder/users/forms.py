from django import forms
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,error_messages={'required':'Email is required'})
    first_name = forms.CharField(required=True, error_messages={'required':'First Name is required'})
    last_name = forms.CharField(required=True, error_messages={'required':'Last Name is required'})
    password1 = forms.CharField(required=True, error_messages={'required':'Password is required'})
    password2 = forms.CharField(required=True, error_messages={'required':'Password Confirmation is required'})

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email address already exists")
        return email


class HeaderForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    middle_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=200)
    website = forms.URLField(required=False)
    linkedin_profile = forms.URLField(required=False)
    phone_number  = forms.SlugField(max_length=100, required=False)
    address = forms.SlugField(max_length=200, required=False)
    professional_summary = forms.CharField(widget=forms.Textarea,required=False)

from django import forms
from django.contrib.auth.models import User
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

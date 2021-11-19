from django.contrib.auth import forms, get_user_model
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import HeaderForm, UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'The account for {email} been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def header(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HeaderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            request.user.first_name = form.cleaned_data['first_name']
            request.user.middle_name = form.cleaned_data['middle_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.website = form.cleaned_data['website']
            request.user.linkedin_profile = form.cleaned_data['linkedin_profile']
            request.user.phone_number  = form.cleaned_data['phone_number']
            request.user.address = form.cleaned_data['address']
            request.user.professional_summary = form.cleaned_data['professional_summary']

            # redirect to a new URL:
            return render(request, 'users/register.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HeaderForm()

    return render(request, 'users/contact.html', {'form': form})

from multiprocessing import current_process
from django.contrib.auth import login
from .forms import DateInput
from django.forms.models import inlineformset_factory
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CVBUser, WorkExperienceEntry
from .forms import HeaderForm, ProfessionalSummaryForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

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

@login_required
def header(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HeaderForm(request.POST, initial={'first_name':request.user.first_name,'last_name':request.user.last_name, 'email':request.user.email })
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            request.user.first_name = form.cleaned_data['first_name']
            request.user.middle_name = form.cleaned_data['middle_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.cv_email = form.cleaned_data['email_on_resume']
            request.user.website = form.cleaned_data['website']
            request.user.linkedin_profile = form.cleaned_data['linkedin_profile']
            request.user.phone_number  = form.cleaned_data['phone_number']
            request.user.address = form.cleaned_data['address']
            request.user.save()

            # redirect to a new URL:
            return redirect('users:summary')

    # if a GET (or any other method) we'll create a blank form
    else:
        initial_data = {}
        initial_data['first_name'] = getattr(request.user,'first_name')
        initial_data['middle_name'] = getattr(request.user,'middle_name')
        initial_data['last_name'] = getattr(request.user,'last_name')
        initial_data['email_on_resume'] = getattr(request.user,'cv_email')
        initial_data['website'] = getattr(request.user,'website')
        initial_data['linkedin_profile'] = getattr(request.user,'linkedin_profile')
        initial_data['phone_number'] = getattr(request.user,'phone_number')
        initial_data['address'] = getattr(request.user,'address')
        form = HeaderForm(initial=initial_data)

    return render(request, 'users/header.html', {'form': form})


@login_required
def summary(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfessionalSummaryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            request.user.professional_summary = form.cleaned_data['professional_summary']
            request.user.save()

            # redirect to a new URL:
            return redirect('users:work')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfessionalSummaryForm(initial={'professional_summary': request.user.professional_summary})

    return render(request, 'users/summary.html', {'form': form})


@login_required
def work_experience(request):
    WorkExperienceEntryFormset = inlineformset_factory(CVBUser,WorkExperienceEntry, fields=('institution','address','starting_date','end_date','current_position'), widgets={"starting_date":DateInput(),"end_date":DateInput(),"current_position":NullBooleanSelect()}, extra=1)
    if request.method == 'POST':
        formset = WorkExperienceEntryFormset(request.POST, request.FILES, instance=request.user)
        # check whether it's valid:
        if formset.is_valid():
            # process the data in form.cleaned_data as required
            request.user.save()
            formset.save()

            # redirect to a new URL:
            return render(request, 'users/projects.html')

    else:
        formset = WorkExperienceEntryFormset()

    return render(request, 'users/work.html', {'formset': formset})


@login_required
def projects(request):
    return render(request, 'users/projects.html')

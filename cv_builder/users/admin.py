from django.contrib import admin
from django.contrib.admin.sites import site
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from .models import CVBUser, Certification, Education, Language, Project, WorkExperienceEntry

# Register your models here.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CVBUser
        fields = ('email','first_name','last_name')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class WorkExperienceEntryInline(admin.TabularInline):
    model = WorkExperienceEntry
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CVBUser
        fields = ('email','first_name','last_name','is_active','is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','first_name','last_name','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Header', {'fields': ('first_name','middle_name','last_name','website','cv_email','linkedin_profile','phone_number','address','professional_summary')}),
    )
    add_fieldsets = (
        (None, {'fields':('email','password1','password2')}),
        ('Header', {'fields': ('first_name','last_name')})
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    inlines = [
        WorkExperienceEntryInline, ProjectInline, LanguageInline, EducationInline, CertificationInline
    ]

admin.site.register(CVBUser, UserAdmin)
admin,site.unregister(Group)
from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from django.forms.widgets import SelectDateWidget, Widget

# Create your models here.
class CVBUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None):
        
        user = self.create_user(
            email,
            first_name = first_name,
            last_name = last_name,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class CVBUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=200)
    cv_email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    phone_number  = models.SlugField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    professional_summary = models.TextField(null=True, blank=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CVBUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    class Meta:
        verbose_name = "user"

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin   


class WorkExperienceEntry(models.Model):
    user = models.ForeignKey(CVBUser, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    starting_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current_position = models.BooleanField()


class Responsability(models.Model):
    work_experience_entry = models.ForeignKey(WorkExperienceEntry, on_delete=models.CASCADE)
    responsability = models.TextField()


class Project(models.Model):
    user = models.ForeignKey(CVBUser, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, blank=True)
    starting_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    project_description = models.TextField()


class Language(models.Model):
    user = models.ForeignKey(CVBUser, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=100, choices=[('limited','Limited Professional Proficiency'),('intermediate','Intermediate Professional Proficiency'),('full','Full Professional Proficiency'),('native','Mother Tongue')])
    proof = models.TextField(blank=True)
    score = models.CharField(max_length=100, blank=True)


class Certification(models.Model):
    user = models.ForeignKey(CVBUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    date_issued = models.DateField()
    additional_info = models.TextField(blank=True)


class Education(models.Model):
    user = models.ForeignKey(CVBUser, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=200)
    starting_date = models.DateField()
    end_date_or_projected_date = models.DateField()
    gpa_or_grade = models.SlugField(max_length=100, blank=True)
    additional_info = models.TextField()
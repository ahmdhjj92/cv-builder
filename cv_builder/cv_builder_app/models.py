from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class ContactInformation(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    phone_number  = models.SlugField(max_length=100)
    address = models.SlugField(max_length=200)


class ProfessionalSummary(models.Model):
    summary = models.TextField()


class Responsability(models.Model):
    responsability = models.TextField()


class WorkExperience(models.Model):
    institution = models.CharField(max_length=200)
    address = models.SlugField(max_length=200)
    starting_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current_position = models.BooleanField()
    responsabilities = models.ManyToManyField(Responsability, related_name='responsablities')


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, blank=True)
    starting_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    project_description = models.TextField()

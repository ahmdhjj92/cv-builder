from django.contrib.admin.decorators import register
from .models import Certification, ContactInformation, Education, Language, ProfessionalSummary, Project, Responsability, WorkExperience
from django.contrib import admin

# Register your models here.
admin.site.register(Education)
admin.site,register(WorkExperience)
admin.site.register(Responsability)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Certification)
admin.site.register(ProfessionalSummary)
admin.site.register(ContactInformation)
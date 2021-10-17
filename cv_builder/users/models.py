from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

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
    website = models.URLField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    phone_number  = models.SlugField(max_length=100)
    address = models.SlugField(max_length=200)
    professional_summary = models.TextField()

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
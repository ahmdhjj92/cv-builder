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
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

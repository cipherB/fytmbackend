from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# custom made user model that overwrites the default user model created by django
class UserAccountManager(BaseUserManager):
    # create user function for all regular login
    def create_user(self, email, name, phone_number, password=None):
        if not email:
            raise ValueError('User must have a valid email address')
        
        email = self.normalize_email(email)

        user = self.model(email=email, name=name, phone_number=phone_number)

        user.set_password(password)
        user.save()

        return user

    # create user function for super users
    def create_superuser(self, email, name, phone_number, password):
        user = self.create_user(email, name, phone_number, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # updates object so all user operations will be carried out on the custom user model
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    def get_full_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number

    def __str__(self):
        return f"{self.email}"


# Create your models here.

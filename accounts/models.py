from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, stack, password, username):
        if not stack:
            raise ValueError("Stack field cannot be empty")
        else:
            user = self.model(stack=stack, username=username)
            user.set_password(password)
            user.save(using=self._db)
            return user
    
    def create_superuser(self, stack, password, username):
        user = self.create_user(stack, password, username)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        # user.set_unusable_password()
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    stack = models.CharField(max_length=100, null=True, blank=True, unique=True)
    mobile_number = models.CharField(max_length=18, null=True, blank=True)
    address = models.CharField(max_length=100)

    USERNAME_FIELD = 'stack' 
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username + " | " + self.stack

    # set this in the settings.py
    # AUTH_USER_MODEL = 'accounts.CustomUser'

# In a custom user model in Django, the USERNAME_FIELD and REQUIRED_FIELDS
# are two attributes used to customize the behavior of the authentication
# system and the user creation process.

# USERNAME_FIELD:

# The USERNAME_FIELD is a string attribute that specifies the field used as
# the unique identifier for the user model. This field is used for 
# authentication purposes, such as logging in or checking if a user already exists.
# The value of USERNAME_FIELD must be a unique field in the user model, and
# it is typically set to a field like username or email.
# When a user logs in or interacts with the authentication system, they will
# provide a value for the USERNAME_FIELD, and Django will use that value to
# retrieve the user from the database for authentication.

# REQUIRED_FIELDS:

# The REQUIRED_FIELDS is a list attribute that specifies additional fields
# that are required when creating a user using the create_user() method of
# the custom user manager.
# When creating a user, the create_user() method requires you to provide a
# value for the USERNAME_FIELD and a password. However, you might want to
# require additional fields when creating a user.
# By including those fields in the REQUIRED_FIELDS list, Django ensures that
# those fields are specified when calling create_user().
# For example, if you have a custom user model with an email as the USERNAME_FIELD
# and you want to require the user to provide a first_name and last_name when
# creating an account, you can set REQUIRED_FIELDS = ['first_name', 'last_name'].
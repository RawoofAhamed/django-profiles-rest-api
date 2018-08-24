from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with custom user model"""

    def create_user(self,email,name,password=None):
        """Creates a new user profile"""

        if not email:
            raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Creates a super user profile"""

        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Represents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def ___str___(self):
        """Django uses this when it needs to convert an object to string """

        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile= models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """retrun the model as string"""

        return self.status_text

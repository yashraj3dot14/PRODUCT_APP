from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as gt
from .managers import CustomUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password= None):# we are overriding method
        if not email:
            raise ValueError('User must have email address!')
        if not username:
            raise ValueError('User must have username!')

        user = self.model(
            email = self.normalize_email(email), #converting lower case
            username = username,
        )
        user.set_password(password)
        user.save(using= self._db) #saving user
        return user

    def create_superuser(self, email, username, password): # we are overriding method
        user = self.model(
            email=self.normalize_email(email),  # converting lower case
            username=username,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db) #saving user
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name= 'email', max_length= 60, unique= True)
    username = models.CharField(max_length= 30, unique= True)
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    date_joined = models.DateTimeField(verbose_name= 'date joined', auto_now_add= True)
    last_login = models.DateTimeField(verbose_name='date joined', auto_now=True)

    is_admin = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)

    USERNAME_FIELD = 'email' #email that we have fetched above
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager() #object of above created MyAccountManager class

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj= None): #method is overridden
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class Post(models.Model):
    user = models.ForeignKey(Account, on_delete= models.CASCADE)
    text = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


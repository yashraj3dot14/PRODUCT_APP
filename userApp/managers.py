from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as gl

class CustomUserManager(BaseUserManager):

    def create_user(self, email,pwd, **extra_fields):
        if not email:
            raise ValueError(gl('Username must be set'))
        #email = self.normalize_email(email)
        user = self.model(username= email, **extra_fields)
        user.set_password(pwd)
        user.save()
        return user


    def create_superuser(self, email, pwd, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') != True:
            raise ValueError(gl('Superuser must have is_staff True'))
        if extra_fields.get('is_superuser') != True:
            raise ValueError(gl('Superuser must have is_superuser True'))

        return self.create_user(email,pwd, **extra_fields)
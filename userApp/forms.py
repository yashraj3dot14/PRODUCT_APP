from django import forms
from .models import Account
from django.db import models
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomAccountCreateForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username','firstname','lastname','email',)

class CustomAccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('username', 'firstname', 'lastname', 'email',)



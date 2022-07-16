from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import customUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= customUser
        fields=["email"]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= customUser
        fields= ["email"]

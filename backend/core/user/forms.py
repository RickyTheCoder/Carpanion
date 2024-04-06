from django.contrib.auth import forms
from .models import User

class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

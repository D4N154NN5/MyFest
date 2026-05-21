from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, label="Vorname")
    last_name = forms.CharField(max_length=50, required=True, label="Nachname")
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=30, required=False, label="Telefon")

    class Meta:
        model = User
        fields = [
            "username", "first_name", "last_name",
            "email", "phone", "password1", "password2",
        ]

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Registration_Form(UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'password1', 'password2')

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField(max_length=50,required=True,help_text='First Name Input', label="First Name")
    lastName = forms.CharField(max_length=50,required=True,help_text='Last Name Input', label="Last Name")

    class Meta:
        model = User
        fields = ['username','email','firstName','lastName','password1','password2']
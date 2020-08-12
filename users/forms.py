from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField(max_length=50,required=True,help_text='First Name Input', label="First Name")
    lastName = forms.CharField(max_length=50,required=True,help_text='Last Name Input', label="Last Name")

    class Meta:
        model = User
        fields = ['username','email','firstName','lastName','password1','password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        firstName = self.cleaned_data["firstName"]
        lastName = self.cleaned_data["lastName"]
        user.first_name = firstName
        user.last_name = lastName
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    firstName = forms.CharField(max_length=50, required=True, label="First Name")
    lastName = forms.CharField(max_length=50, required=True, label="Last Name")

    class Meta:
        model = User
        fields = ['username', 'email', 'firstName', 'lastName']

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        firstName = self.cleaned_data["firstName"]
        lastName = self.cleaned_data["lastName"]
        user.first_name = firstName
        user.last_name = lastName
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

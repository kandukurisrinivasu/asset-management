from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserData


class UserDataForm(forms.ModelForm):
    location = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Location'}))
    team = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Team'}))
    group = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Group'}))
    phonenumber = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Phone Number'}))

    class Meta:
        model = UserData
        fields = ('location', 'team', 'group', 'phonenumber')

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",
                "class": "form-control"
            }
        ))
    Location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Location",
                "class": "form-control",
            }
        ))

    Team_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Team Name",
                "class": "form-control"
            }
        ))
    Group =forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Group",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PasswordReset(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email","class": "form-control"}))


class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password',)
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
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
                "placeholder": "Username",
                "class": "form-control"
            }
        ),required=True)

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Full Name",
                "class": "form-control"
            }
        ),required=True)
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ),required=True)
    Location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Location",
                "class": "form-control",
            }
        ),required=True)

    Team_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Team Name",
                "class": "form-control"
            }
        ),required=True)
    Group = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Group",
                "class": "form-control"
            }
        ),required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ),required=True)
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ),required=True)

    class Meta:
        model = User
        fields = ('username','name', 'email','Location','Team_name','Group','password1', 'password2')

    def save(self,commit=True):
        user=super(SignUpForm,self).save(commit=False)
        user.name=self.cleaned_data['name']
        user.email=self.cleaned_data['email']
        user.Location=self.cleaned_data['Location']
        user.Team_name=self.cleaned_data['Team_name']
        user.Group=self.cleaned_data['Group']

        if commit:
            user.save()

        return user



class PasswordReset(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email","class": "form-control"}))


class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password',)

class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')
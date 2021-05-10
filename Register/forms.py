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

class signupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "col-sm col-form-label"}))
    first_name = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name=forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    location = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Location'}))
    team = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Team'}))
    group = forms.CharField(label="", max_length=50,widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Group'}))
    phonenumber = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Phone Number'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password check", "class": "form-control"}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','location','team','group','phonenumber', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Windows NT ID</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification</small></span>'

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))

class PasswordReset(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder" : "Email","class": "form-control"}))


class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password',)
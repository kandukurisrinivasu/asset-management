from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core import validators

## check custom #validation for the password
#def check_size(value):
#    if len(value)<6:
#        raise forms.ValidationError("password is too short")

#class SignUp(forms.Form):
#    first_name = forms.CharField()
#    last_name = forms.CharField()
#    email = forms.EmailField(help_text = 'write your email', )
#    Mobile = forms.IntegerField()
#    Department =forms.CharField()
#    Group=forms.IntegerField()
#    Employee_no=forms.IntegerField()
#    Team_name=forms.CharField()
#    age = forms.IntegerField()
#   upload_your_photo=forms.FileField()

#class editForm(forms.Form):

#    first_name = forms.CharField()
#    last_name = forms.CharField()
#    email = forms.EmailField(help_text = 'write your email', )
#    Mobile = forms.IntegerField()
#    Department =forms.CharField()
#    Group=forms.IntegerField()
#    Employee_no=forms.IntegerField()
#    Team_name=forms.CharField()
#    age = forms.IntegerField()
#    upload_your_photo=forms.FileField()

class asset(forms.ModelForm):
    class Meta:
        model= assetOwner
        fields= "__all__"

        

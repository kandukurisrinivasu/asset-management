from django import forms
from .models import UserProfile,Asset_details,Lab_event,Setup_details,EventMember
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

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

#class asset(forms.ModelForm): Previous one
#    class Meta:
#        model= assetOwner
#        fields= "__all__"

        
class UserProfileForm(forms.ModelForm):
    user_name= forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Username'}))
    Group= forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Group Name'}))
    Team_name= forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Team name'}))
    Location= forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Loaction'}))
    Phone= forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':'Phone number'}))
    class Meta:
        model=UserProfile
        fields=('user_name','Group','Team_name','Location','Phone')

class AssetDetailsForm(forms.ModelForm):
    Asset_no =  forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Number'}))
    Owner =  forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Owner'}))
    Asset_type = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Type'}))
    Team_name=forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Team name'}))
    Group=Team_name=forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Group'}))
    working_status =  forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Working status'}))
    Remark =  forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Remark'}))
    Product_line =  forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Product Line'}))


    class Meta:
        model=Asset_details
        fields=('Asset_no','Owner','Asset_type','working_status','Remark','Product_line')

class LabEventForm(forms.ModelForm):
    class Meta:
        model=Lab_event
        fields = ('Setup_name','Title', 'Description', 'Start_date', 'End_date', 'Start_time', 'End_time')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%dT%H:%M'),
            'start_time': forms.DateInput(attrs={'type': 'time'}, format='%Y-%m-%dT%H:%M'),
            'end_time': forms.DateInput(attrs={'type': 'time'}, format='%Y-%m-%dT%H:%M'),
        }
        exclude = ['user']

class setupDetailsForm(forms.ModelForm):
    Host_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Host name'}))
    FQDN = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'FQDN'}))
    OS = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'os'}))
    COM_port_details = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'COM PORT DETAILS'}))
    Other_details = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'other details'}))

    class Meta:
        model=Setup_details
        fields=('Host_name','FQDN','OS','COM_port_details','Other_details')

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


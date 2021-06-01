from django import forms
from .models import UserProfile,Asset_details,Event,Setup_details,EventMember
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

#class AssetDetailsForm(forms.Form):
#    AssetNo          = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Number'}))
#    Owner            = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Owner'}))
#    AssetTypeModel   = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Type/Model'}))
#    Group            = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Group'}))
#    TeamName         = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Team'}))
#    Loc              = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Location'}))
#    ProductLine      = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Product line'}))
#    Remark           = forms.CharField(label="", max_length=400, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Remark'}))




class AssetDetailsForm(forms.ModelForm):
    AssetNo          = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Number'}))
    Owner            = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Owner'}))
    AssetTypeModel   = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Asset Type/Model'}))
    Group            = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Group'}))
    TeamName         = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Team'}))
    Loc              = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Location'}))
    ProductLine      = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Product line'}))
    Remark           = forms.CharField(label="", max_length=400, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Remark'}))

    class Meta:
        model=Asset_details
        fields=[
            "AssetNo",
            "Owner",
            "AssetTypeModel",
            "Group",
            "TeamName",
            "Loc",
            "ProductLine",
            "Remark",
        ]



class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    fields = ('title','description','start_date','end_date','start_time','end_time')
    widgets = {
      'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%dT%H:%M'),
      'end_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%dT%H:%M'),
      'start_time': forms.DateInput(attrs={'type': 'time'}, format='%Y-%m-%dT%H:%M'),
      'end_time': forms.DateInput(attrs={'type': 'time'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    """A test!"""
    print("Test.")
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%H:%M',)
    self.fields['end_time'].input_formats = ('%H:%M',)


#class setupDetailsForm(forms.Form):
#    Host_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Host name'}))
#    FQDN = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'FQDN'}))
#    OS = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'OS'}))
#    COM_port_details = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Com Port details'}))
#    Other_details = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Other details'}))


class setupDetailsForm(forms.ModelForm):
    Host_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Host name'}))
    FQDN = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'FQDN'}))
    OS = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'OS'}))
    COM_port_details = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Com Port details'}))
    Other_details = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'col-sm col-form-label', 'placeholder':'Other details'}))

    class Meta:
        model=Setup_details
        fields=[
            "Host_name",
            "FQDN",
            "OS",
            "COM_port_details",
            "Other_details",
        ]



class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class AddMemberForm(forms.ModelForm):

    class Meta:
        model=EventMember
        fields = ['user']

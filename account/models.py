from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):  ## name of the table
    user_name=models.OneToOneField(User,on_delete=models.CASCADE) # one to one relationship in database
    # One-to-one relationships occur when there is exactly one record in the first table that corresponds to one record in the related table

    Group=models.CharField(max_length=30,default='EBB')
    Team_name=models.CharField(max_length=30,default='EBB')
    Location=models.CharField(max_length=30,default='BAN')
    Phone=models.CharField(max_length=30,default='0000000000')

    def __str__(self):
        return self.user_name

class Asset_details(models.Model):
    AssetNo = models.CharField(max_length=50)
    Owner = models.CharField(max_length=50)
    AssetTypeModel = models.CharField(max_length=50)
    Group = models.CharField(max_length=50)
    TeamName = models.CharField(max_length=50)
    ProductLine = models.CharField(max_length=50)
    Remark = models.CharField(max_length=400)


    def __str__(self):
        return self.AssetNo

class Lab_event(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)# The user name from main table to base table will be same
    Title=models.CharField(max_length=200,unique=True)
    Description=models.TextField()
    Start_date=models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    End_date=models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    Start_time=models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    End_time=models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    created_date=models.DateTimeField(auto_now_add=True) # auto now add means fill with current date.

    def __str__(self):
        return self.Title

    def get_url(self):
        return reverse('authentication:Lab-event',args=(self.id,)) # This reverse a large variety
    # of regular expression in URL patterns.

    @property
    def get_html_url(self):
        print("get_html_url")
        print(self.id)
        url=reverse('Lab-event', args=(self.id,))
        return f'<a href="{url}"> {self.Title} </a>'


class Setup_details(models.Model):
    Host_name=models.CharField(max_length=30)
    FQDN=models.CharField(max_length=20,default='si-z0z15.st.de.bosch.com')
    OS=models.CharField(max_length=20)
    COM_port_details=models.CharField(max_length=50)
    Other_details=models.TextField()

    def __str__(self):
        return self.Host_name

class EventMember(models.Model):
    event=models.ForeignKey(Lab_event,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together=['event', 'user']

        def __str__(self):
            return str(self.user)

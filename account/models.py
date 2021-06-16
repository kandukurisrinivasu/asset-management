from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
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
    Loc=models.CharField(max_length=50)
    ProductLine = models.CharField(max_length=50)
    Remark = models.CharField(max_length=400)


    def __str__(self):
        return self.AssetNo

    def get_absolute_url(self):
        return reverse('asset_search_display', args=(self.id,))

    @property
    def get_html_url(self):
        print("get_html_url")
        print(self.id)
        url = reverse('asset_search_display', args=(self.id,))
        return f'<a href="{url}"> {self.AssetNo} </a>'

#class Lab_event(models.Model):
#    user=models.ForeignKey(User,on_delete=models.CASCADE)# The user name from main table to base table will be same
#    Title=models.CharField(max_length=200,unique=True)
#    Description=models.TextField()
#    Start_date=models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
#    End_date=models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
#    Start_time=models.TimeField(auto_now_add=False, auto_now=False, blank=True)
#    End_time=models.TimeField(auto_now_add=False, auto_now=False, blank=True)
#    created_date=models.DateTimeField(auto_now_add=True) # auto now add means fill with current date.

#    def __str__(self):
#        return self.Title

 #   def get_absolute_url(self):
 #       return reverse('authentication:lab_event_details', args=(self.id,)) # This reverse a large variety
    # of regular expression in URL patterns.

#    @property
#    def get_html_url(self):
#        print("get_html_url")
#        print(self.id)
#        url = reverse('lab_event_details', args=(self.id,))
 #       return f'<a href="{url}"> {self.Title} </a>'



class Setup_details(models.Model):
    lab_name = models.CharField(max_length=30)
    Host_name=models.CharField(max_length=30)
    FQDN=models.CharField(max_length=50,default='si-z0z15.st.de.bosch.com')
    OS=models.CharField(max_length=20)
    COM_port_details=models.CharField(max_length=50)
    Other_details=models.TextField()

    def __str__(self):
        return self.lab_name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    lab_name=models.ForeignKey(Setup_details,on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    start_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    end_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('time out', 'Time Out'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        return self.title

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True

        return overlap

    def get_absolute_url(self):
        return reverse('event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        print("get_html_url")
        print(self.id)
        url = reverse('event-detail', args=(self.id,))
        return f' Booked : {self.lab_name} <br><br>'\
               f' Start time : {self.start_time} <br><br>'\
               f'End time : {self.end_time} <br><br>'\
               f'End date :{self.end_date} <br><br>' \
               f'<a href="{url}"> Details </a> <br><br>'

    def clean(self):
        if  self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(start_date=self.start_date)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'Sorry this time slot is already booked with this time: ' + str(event.start_date) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))



class EventMember(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together=['event', 'user']

        def __str__(self):
            return str(self.user)


class Feedback(models.Model):
    Name = models.CharField(max_length=50)
    email=models.EmailField(max_length=25)
    message =models.TextField()
    def __str__(self):
        return self.Name
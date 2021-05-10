from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, default='BAN' )
    team = models.CharField(max_length=30, default='EBB')
    group = models.CharField(max_length=30,default='EBB' )
    phonenumber = models.CharField(max_length=30, default='0000000000')

    def __str__(self):
        return self.user
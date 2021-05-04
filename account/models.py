from django.db import models

# Create your models here.
class assetOwner(models.Model):  ## name of the table
    sID=models.IntegerField()
    f_name=models.CharField(max_length=100, blank=False)
    l_name=models.CharField(max_length=100, blank=False)
    email=models.EmailField()
    Mob=models.IntegerField()
    age=models.IntegerField()
    upload_photo=models.ImageField()
    group=models.CharField(max_length=100, blank=False)
    team_name=models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.f_name

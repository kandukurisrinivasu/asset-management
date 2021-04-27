from django.db import models

# Create your models here.
class assetOwner(models.Model):  ## name of the table
    f_name=models.CharField(max_length=100, blank=False)
    l_name=models.CharField(max_length=100, blank=False)

    asset_num=models.IntegerField()
    asset_type=models.CharField(max_length=100, blank=False)
    group=models.CharField(max_length=100, blank=False)
    team_name=models.CharField(max_length=100, blank=False)

    def __str__(self): ## this function is used to represent the certain object
        return 'First name: {0} Asset num :{1}'.format(self.f_name, self.l_name)





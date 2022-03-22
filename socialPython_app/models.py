import email
from django.db import models

# Create your models here.
class userModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=15, unique=True, default='SOME STRING')
    email = models.EmailField(max_length=60)
    address = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ',' + ' ' + 'UserName: ' + self.user_name

        # return str(self.id)+' '+self.name+' '+self.email+' '+self.address

class userProfileModel(models.Model):
    gender = models.CharField(max_length=15)    
    job = models.CharField(max_length=35)
    education = models.CharField(max_length=30)
    work_experience = models.CharField(max_length=35)
    description = models.CharField(max_length=60)
    user = models.ForeignKey(userModel,related_name='relation', on_delete=models.CASCADE)
    


# GENDER = [('male','MALE'),('female', 'FEMALE')]
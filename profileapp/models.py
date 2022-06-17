from django.db import models
from urllib.parse import urljoin
from django.contrib.auth.models import User
# Create your models here.
a='http://127.0.0.1:8000/get/ppp/'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    name = models.CharField(max_length=200, null=True)

    title = models.CharField( max_length=200, null=True)

    desc = models.CharField( max_length=200, null=True)

    profile_img =  models.ImageField(default = 'media/default.png', upload_to = 'media', null = True, blank = True)
    profile_url = models.URLField(default=f'{a}{user}')

class Education(models.Model):
    user_name=models.ManyToManyField(User)
    Board = (('*', 'Select Board'),('cbase','CBSE'),('up','U.P.'),('icse','ICSE'),('Biahr','Bihar Board'))
    class_10th = models.CharField(null = True,max_length=15, choices=Board)
    class_10th_School = models.CharField(null = True,max_length=100)
    Start_date_10th = models.DateField(null = True)
    End_date_10th = models.DateField(null = True)
    percentage_10th = models.FloatField(null = True)
    class_12th = models.CharField(null = True,max_length=15, choices=Board)
    class_12th_School = models.CharField(null = True,max_length=100)
    Start_date_12th = models.DateField(null = True)
    End_date_12th = models.DateField(null = True)
    percentage_12th = models.FloatField(null = True)
    courses=(('*', 'Select Course'),('B.Sc', 'Bachelor of Science'),('B.tech','Bachelor of Technology'),('M.Sc', 'Masters of Science'))
    graduation=models.CharField(max_length=15,choices=courses)
    graduation_percentage=models.FloatField(null = True)
    graduation_start_date = models.DateField(null = True)
    graduation_end_date= models.DateField(null = True)

    def __str__(self):
        return f"{self.user.username}'s profile"
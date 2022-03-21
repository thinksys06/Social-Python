import email
from django.db import models

# Create your models here.
class userModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=602)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.id+self.name+self.email+self.address
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       created = Profile.objects.get_or_create(user=instance)
@receiver(user_logged_in,sender=User)
def login_done(sender,request,user,**kwargs):
    print('-------------------------')
    print('login done ')
    return redirect('home')
#user_logged_in.connect(login_success,sender=userModel)

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print('------------------------')
    print('your logout')


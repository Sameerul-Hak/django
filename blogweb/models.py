from django.contrib.auth.models import User
from django.db import models
import datetime
import os
from django.utils import timezone
# Create your models here.

def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
class addblogs(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    description=models.TextField(max_length=1000)
    related=models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Projects(models.Model):
    CHOICES = [
        ('app', 'Mobile App'),
        ('web', 'Web App'),
        ('other', 'Other')
    ]
    project_name=models.CharField(max_length=100)
    phone_number=models.BigIntegerField()
    basic_idea=models.TextField(max_length=500)
    project_type = models.CharField(max_length=5, choices=CHOICES)

    def __str__(self):
        return self.project_name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

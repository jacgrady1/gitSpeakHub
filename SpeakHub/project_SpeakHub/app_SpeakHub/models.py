from django.db import models

from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError

# class Profile(models.Model):
#     intro = models.CharField(max_length=200)
#     dob = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     user = models.OneToOneField(User)
#     gender = models.CharField(max_length=50)
#     picture = models.ImageField(upload_to="profile-photos", blank=True)
    
#     def __unicode__(self):
#         return self.user

class Audio(models.Model):
    #user = models.ForeignKey(User)
    audiofile = models.FileField(upload_to='audios/%Y/%m/%d')
    text = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ensure users can't be friends with themselves
        if self.text and self.audiofile:
            #raise ValidationError("Nothing there")
            super(Audio, self).save(*args, **kwargs)


# class Tagging(models.Model):
#     user = models.ForeignKey(User)
#     starttime= models.CharField(max_length=50) # stores formated time 00:01
#     startsecond= models.CharField(max_length=200) # stores raw second 1.0002
#     text = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     video = models.ForeignKey(Document)

#     def __unicode__(self):
#         return self.text



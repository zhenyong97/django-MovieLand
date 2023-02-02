from django.db import models
from django.contrib.auth.models import AbstractUser

from movieland.apps import defs

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=128, blank=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=defs.ROLE_CHOICES,
                                            blank=False, null=False)
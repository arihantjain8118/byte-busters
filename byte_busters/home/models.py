from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileType(models.Model):
    name = models.CharField(max_length=20)

# class Profile(models.Model):
    # profile_type = 
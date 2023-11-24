# userprofile_app/models.py
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    about = models.TextField()
    areas_of_interest = models.TextField()

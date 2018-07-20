from django.db import models
from django.contrib import admin

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)




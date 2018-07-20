from django.db import models
from django.contrib import admin
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    content =models.TextField()
    timestamp = models.DateTimeField()

class BolgAdmin(admin.ModelAdmin):
    lsit_display = ('title','content','timestamp')

admin.site.register(Blog,BolgAdmin)
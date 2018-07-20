from django.db import models
from django.contrib import admin
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    # blog connet
    class Meta:
        ordering = ('-timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
    list_dispaly = ('title', 'timestamp')
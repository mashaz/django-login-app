from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	usertype = models.CharField(max_length=10,default="1")
	upload_sum = models.IntegerField(default="0")
	
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(User)
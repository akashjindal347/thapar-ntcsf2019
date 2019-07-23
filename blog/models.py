from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
   
    name = models.CharField(max_length = 100)
    description = models.TextField(default = '')
    link = models.CharField(max_length = 100,default = '')

    def __str__(self):
        return str(self.name)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
   
    name = models.CharField(max_length = 100)
    description = models.TextField(default = '')
    link = models.CharField(max_length = 100,default = '',null= True,blank = True)

    def __str__(self):
        return str(self.name)

class AboutTheConference(models.Model):
   
    description = models.TextField(default = '')
    link = models.CharField(max_length = 100,default = '',null= True,blank = True)

    def __str__(self):
        return str(self.description)

class CallForPaper(models.Model):
   
    description = models.TextField(default = '')

    def __str__(self):
        return str(self.description)


class ImportantDate(models.Model):

    description = models.TextField(default = '')
    date = models.TextField(default = '')
    highlighted = models.TextField(default = '', null=True)
    
    def __str__(self):
        return str(self.date)

class Speaker(models.Model):
   
    name = models.CharField(default = '', max_length=50)

    def __str__(self):
        return str(self.name)

class Organiser(models.Model):
   
    name = models.CharField(default = '', max_length=50)

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
   
    description = models.TextField(default = '')

    def __str__(self):
        return str(self.description)

class RegistrationContact(models.Model):

    description = models.TextField(default = '')
    link = models.CharField(max_length = 100,default = '',null= True,blank = True)

    def __str__(self):
        return str(self.description)

class Announcement(models.Model):

    description = models.TextField(default = '')
    title = models.CharField(max_length = 100,default = '')
    highlights = models.TextField(default = '')

    def __str__(self):
        return str(self.title)

class BankDetail(models.Model):

    description = models.TextField(default = '')

    def __str__(self):
        return str(self.description)

class RegistrationFee(models.Model):

    description = models.TextField(default = '')

    def __str__(self):
        return str(self.description)

class AccomodationAndTravel(models.Model):

    description = models.TextField(default = '')

    def __str__(self):
        return str(self.description)




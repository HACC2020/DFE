from django.db import models

# Create your models here.
class applications(models.Model):
    name = models.CharField(max_length=100)
    ownerAgencyName = models.CharField(max_length=100)

class projects(models.Model):
    ownerAgencyName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class usergroups(models.Model):
    name = models.CharField(max_length=100)

# class averages(models.Model):

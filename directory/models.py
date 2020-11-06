from django.db import models

# Create your models here.
class applications(models.Model):
    name = models.CharField(max_length=100)
    ownerAgencyName = models.CharField(max_length=100)

    def __str__(self):
        return self.Applications

class projects(models.Model):
    ownerAgencyName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.Projects

    '''
    when call upon this in admin, displays name within admin,
    helps populate table in admin
    ex. return self.breed (return data in breed colummn)
    '''

class usergroups(models.Model):
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=100)

    def __str__(self):
        return self.Agencies

class percents(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()

    def __str__(self):
        return self.Percents


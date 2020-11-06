from django.db import models

# Create your models here.
class applications(models.Model):
    name = models.CharField(max_length=100)
    ownerAgencyName = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class projects(models.Model):
    ownerAgencyName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    #when call upon this in admin, displays name within admin,
    #helps populate table in admin
    #ex. return self.breed (return data in breed colummn)

class usergroups(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

'''
    class Meta:
        ordering = ['name']
'''
# class averages(models.Model):

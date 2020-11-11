'''
    Declarations of entries in the mongo database
    Copyright (C) 2020  DFE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from django.db import models

# Create your models here.


class applications(models.Model):
    name = models.CharField(max_length=100)
    ownerAgencyName = models.CharField(max_length=100)
    subOwnerAgencyName = models.CharField(max_length=100)
    successors = models.CharField(max_length=100)
    leadingBusinessCapability = models.CharField(max_length=100)
    businessCriticality = models.CharField(max_length=100)
    functionalFit = models.CharField(max_length=100)
    technicalFit = models.CharField(max_length=100)
    lifecycle_plan = models.CharField(max_length=100)
    lifecycle_active = models.CharField(max_length=100)
    lifecycle_endOfLife = models.CharField(max_length=100)
    timeTag = models.CharField(max_length=100)
    hostingTypeTag = models.CharField(max_length=100)
    majorInformationSystemsTag = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class projects(models.Model):
    ownerAgencyName = models.CharField(max_length=100)
    subOwnerAgencyName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    applications = models.CharField(max_length=100)
    projectStatus = models.CharField(max_length=100)
    businessValue = models.CharField(max_length=100)
    projectRisk = models.CharField(max_length=100)
    lifecycleCustom_planningStarted = models.CharField(max_length=100)
    lifecycleCustom_approved = models.CharField(max_length=100)
    lifecycleCustom_projectedStart = models.CharField(max_length=100)
    lifecycleCustom_cancelled = models.CharField(max_length=100)
    lifecycleCustom_projectedCompletion = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class usergroups(models.Model):
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class percents(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()

    def __str__(self):
        return self.name


class contactforms(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
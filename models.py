# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class Job(models.Model):
    order = models.IntegerField(default=0)
    company = models.CharField(max_length=128)
    language = models.CharField(max_length=5, choices=settings.LANGUAGES)
    location = models.CharField(max_length=128, null=True,blank=True)
    position = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.company + ' - ' + self.position

    class Meta:
        ordering = ['order']


class Education(models.Model):
    school = models.CharField(max_length=128)
    degree = models.CharField(max_length=50)
    major = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=5, choices=settings.LANGUAGES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.school

    class Meta:
        ordering = ['-end_date']

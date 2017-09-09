# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Job, Education
from django.utils import translation

# Create your views here.
def CV(request):
    language=translation.get_language()
    jobs = Job.objects.filter(language=language)
    educations = Education.objects.filter(language=language)

    return render(request, 'cv/index.html', { 'jobs' : jobs, 'educations' : educations})


def About(request):
    return render(request, 'cv/about.html', {})
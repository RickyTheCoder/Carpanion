# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# core/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my app!")  # Or render a template

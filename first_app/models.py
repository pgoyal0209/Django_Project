# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_by = models.ForeignKey(User, null=True, related_name='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
 
from login.models import Student,SS

admin.site.register(Student)
admin.site.register(SS)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SS(models.Model):
	#id = models.IntegerField(primary_key=True)
	name=models.CharField(max_length=50)
	username=models.CharField(max_length=50)


class Student(models.Model):
	#id = models.IntegerField(primary_key=True)
	name=models.CharField(max_length=50)
	username=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50)
	college=models.CharField(max_length=50)

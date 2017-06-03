# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import SS,Student	
#from models import 
from django.http import HttpResponse
# Create your views here.


def add(request,name,username,password,college):
	
	#data={'success':False}
	#queryset = Student.objects.all()
	
	a = Student()
	a.name =name
	a.username =username
	a.password =password
	a.college =college
	a.save()
	return HttpResponse("blahblah")
				

def check(request,name,username):
	a=SS()
	a.name=name
	a.username=username
	a.save()
	return HttpResponse("blahblah")


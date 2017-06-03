# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from login.models import SS,Student	
#from models import 
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.


def insert(request,name,username,password,college):
	
	#data={'success':False}
	#queryset = Student.objects.all()
	
	a = Student()
	a.name =name
	a.username =username
	a.password =password
	a.college =college
	a.save()
	return HttpResponse("blahblah")
				

def getdata(request,name,username):
	
	
	q=Student.objects.filter(username=username)	
	qq=q.values()
	print q.values()
	
	qlist=[]
	for i in qq:
		qlist.append(i)
	#print (JsonResponse(qlist,safe=False))
	return JsonResponse(qlist,safe=False)	
	#return HttpResponse('gfh')


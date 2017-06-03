"""student_details URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from login import views

 

urlpatterns = [
    #url(r'^check/', views.check),
    #url(r'^check/name=(<name>[a-z A-Z]+)&username=(<username>[a-zA-Z_]+)&password=(<password>[A-Za-z0-9@#$%^&+=]{8,})&college=(<college>[a-zA-Z_]+)',views.add),
    url(r'^insert/'+'name='+'(?P<name>[a-z A-Z]+)&'+'username='+'(?P<username>[a-z A-Z_]+)&'+'password='+'(?P<password>[A-Za-z0-9@#$%^&+=]{8,})&'+'college='+'(?P<college>[a-zA-Z_]+)',views.insert),
    #url(r'^gd/'+'name='+'(?P<name>[a-z A-Z]+)&'+'username='+'(?P<username>[a-z A-Z_]*)&'+'password='+'(?P<password>[A-Za-z0-9@#$%^&+=]{8,})&'+'college='+'(?P<college>[a-zA-Z_]+)',views.getdata),
    #url(r'^getdata/'+'name='+'(?P<name>[a-z A-Z]+)&'+'username='+'(?P<username>[a-z A-Z_]*)',views.getdata),
    url(r'^getdata/'+'name='+'(?P<name>[a-z A-Z_]+)&'+'username='+'(?P<username>[a-z A-Z_]+)',views.getdata),
    #url(r'^check/',views.add),
    
    url(r'^admin/',admin.site.urls),
]

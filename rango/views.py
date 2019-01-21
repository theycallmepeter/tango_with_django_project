from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!\n<br/><a href =\"/rango/about\">About this page</a>")
# Create your views here.

def about(request): 
	return HttpResponse("<a href=\"/rango/\"> Index</a>")

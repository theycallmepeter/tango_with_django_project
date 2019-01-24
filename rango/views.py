from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)

	# return HttpResponse("Rango says hey there partner!\n<br/><a href =\"/rango/about\">About this page</a>")
# Create your views here.

def about(request): 

	context_dict = {'author_name': "Peter"}
	return render(request, 'rango/about.html', context=context_dict)
	# return HttpResponse("<a href=\"/rango/\"> Index</a>")

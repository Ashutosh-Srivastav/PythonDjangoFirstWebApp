from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World, this is Poll View")

# Create your views here.

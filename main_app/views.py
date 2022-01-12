from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import dogs as dogs 

# Create your views here.

def home(request):
    return HttpResponse('hello world')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def members(requests):
  return HttpResponse("Hello world!")

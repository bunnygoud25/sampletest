from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hey bunny")
def bunny(request):
    return HttpResponse("hey mukesh")

from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('App de nome todos')
# Create your views here.

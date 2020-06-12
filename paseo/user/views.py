from django.shortcuts import render
#from django.http import
from .models import User


def log(request):
  return  render(request,'user/login.html')


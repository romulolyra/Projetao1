#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def inicial(request):
 return render(request, 'app/inicial.html')

def sobre(request):
 return render(request, 'app/sobre.html')

def log(request):
  return render(request, 'app/login.html')


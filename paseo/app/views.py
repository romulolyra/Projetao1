from .forms import UserForm
from .models import   User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


def inicial(request):
    usuarios = User.objects.all()
    return render(request, 'app/inicial.html',{'usuarios':usuarios})

def sobre(request):
    return render(request, 'app/sobre.html')

def log(request):
    return render(request, 'app/login.html')

def cadas(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/inicial')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()


    return render(request, 'app/cadastro.html',{'form':form})


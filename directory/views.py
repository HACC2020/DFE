from django.shortcuts import render
from .models import usergroups
from .models import applications
from .models import projects
from .models import percents

# Create your views here.

#def work(request, folder_id):

#does organization exist within database

def home(request):
    return render(request, 'directory.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def departments(request):
    return render(request, 'departments.html')

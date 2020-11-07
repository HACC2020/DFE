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


def departments(request, page):
    usergroups_var = usergroups.objects.all().order_by('parent')
    subdepartments = []
    page_var = len(usergroups_var)/25
    page_var = round(page_var)
    t = 0
    p = 25
    if int(page) != 1:
        for i in range(0,int(page)):
            t += 25
            p += 25
    for i in range(t,p):
        subdepartments.append(usergroups_var[i])
    return render(request, 'departments.html', {'name': subdepartments})


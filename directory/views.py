from django.shortcuts import render
from .models import usergroups
from .models import applications
from .models import projects
from .models import percents

# Create your views here.


def home(request):
    return render(request, 'directory.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def departments(request, page):
    usergroups_var = usergroups.objects.all().order_by('parent')
    pages = []
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
        try:
            subdepartments.append(usergroups_var[i])
        except IndexError:
            pass

    for i in range(1,int(page_var)+1):
        pages.append(i)

    return render(request, 'departments.html', {'name': subdepartments, 'page': pages})

#REPLACE VARIABLES WITH APPLICATIONS

def applications(request):
    applications_var = applications.objects.all().order_by('name')
    projects = []
    return render(request, 'applications.html', {'name': projects})




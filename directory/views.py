from django.shortcuts import render
from .models import usergroups, applications, projects, percents

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def departments(request, page):
    usergroups_var = usergroups.objects.all().order_by('parent')

    filterUserGroup = []

    for i in usergroups_var:
        if applications.objects.filter(ownerAgencyName=i) is not None:
            filterUserGroup.append(i)

    pages = []
    subdepartments = []
    page_var = len(filterUserGroup)/25
    page_var = round(page_var)
    t = 0
    p = 25

    if int(page) != 1:
        for i in range(0,int(page)):
            t += 25
            p += 25

    for i in range(t,p):
        try:
            subdepartments.append(filterUserGroup[i])
        except IndexError:
            pass

    for i in range(1,int(page_var)+1):
        pages.append(i)

    return render(request, 'departments.html', {'name': subdepartments, 'page': pages})


#REPLACE VARIABLES WITH APPLICATIONS


def application(request, departments):
    applications_var = applications.objects.filter(ownerAgencyName=departments)
    subdepartments = usergroups.objects.filter(name=departments)
    apps = []
    if subdepartments is not None:
        for i in range(0,len(applications_var)):
            apps.append((applications_var[i]))
        # print(applications_var)
        return render(request, 'applications.html', {'appinfo': apps})
    else:
        return(request, 'error.html')

#def project(request,):










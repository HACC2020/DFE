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
    usergroups_var = usergroups.objects.all()
    filterUserGroup = []

    for i in usergroups_var:
        if projects.objects.filter(ownerAgencyName=i) is not None:
            filterUserGroup.append(i)

    filterUserGroup.sort(key=lambda x:x.parent, reverse=False)
    print(filterUserGroup)

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


def application(request, departments):
    applications_var = applications.objects.filter(subOwnerAgencyName=departments)
    subdepartments = usergroups.objects.filter(name=departments)
    apps = []
    if subdepartments is not None:
        for i in range(0,len(applications_var)):
            apps.append((applications_var[i]))
        #print(apps)
        return render(request, 'applications.html', {'apps': apps})
    else:
        return render(request, 'error.html')


def project(request, applications):
    projects_var = projects.objects.filter(applications=applications)
    appinfo = applications.objects.filter(name=applications)
    project = []
    if appinfo is not None:
        for i in range(0, len(projects_var)):
            project.append((projects_var[i]))
        print(project)

        return render(request, 'applications.html', {'projects': project})
    else:
        return render(request, 'error.html')


def projectpage(request, projects):
    projectdata_var = projects.objects.filter(name=projects)
    projectdata = []
    for i in projectdata_var:
        projectdata.append(projectdata_var[i])
        print(projectdata)
    return render(request, 'project.html', {'projectdata': projectdata})








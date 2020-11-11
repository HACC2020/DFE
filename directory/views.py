'''                   
    Process URL requests
    Copyright (C) 2020  DFE               
                                           
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.                         
                                                          
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.                      
                                                               
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
    Application_var = applications.objects.all()
    filterUserGroup = []

    for i in usergroups_var:
        for t in Application_var:
            if i.name == t.subOwnerAgencyName:
                filterUserGroup.append(i)

    for i in usergroups_var:
        for t in Application_var:
            if i.name == t.ownerAgencyName:
                filterUserGroup.append(i)

    filterUserGroup = list(set(filterUserGroup))

    #print(filterUserGroup)


    pages = []
    subdepartments = []
    page_var = len(filterUserGroup) / 25
    page_var = round(page_var)
    t = 0
    p = 25

    if int(page) != 1:
        for i in range(0, int(page)):
            t += 25
            p += 25

    for i in range(t, p):
        try:
            subdepartments.append(filterUserGroup[i])
        except IndexError:
            pass

    for i in range(1, int(page_var)):
        pages.append(i)

    return render(request, 'departments.html', {'name': subdepartments, 'page': pages})


def application(request, departments):
    applications_var = applications.objects.filter(subOwnerAgencyName=departments)
    applications_var2 = applications.objects.filter(ownerAgencyName=departments)
    subdepartments = usergroups.objects.filter(name=departments)
    project_filter = projects.objects.filter(subOwnerAgencyName=departments)
    apps = []
    project = []

    if len(subdepartments) != 0:
        for i in range(0,len(applications_var)):
            apps.append((applications_var[i]))
        for i in range(0,len(applications_var2)):
            apps.append(applications_var2[i])
        #print(apps)
        for i in range(0,len(project_filter)):
            try:
                project_filter[i].applications=project_filter[i].applications.split(';')
                #print(project_filter[i])
            except AttributeError:
                pass
            project.append(project_filter[i])
        #print(project)
        return render(request, 'applications.html', {'apps': apps, 'projects': project})
    else:
        return render(request, 'error.html')


def projectpage(request, project):
    projects_var = projects.objects.filter(name=project)
    for i in projects_var:
        listofapps = i.applications.split(';')
    #print(projects_var)
    return render(request, 'project.html', {'projectinfo': projects_var, 'listofapps': listofapps})







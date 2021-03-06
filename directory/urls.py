'''                   
    URL dispatcher entries
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contact, name='contacts'),
    path('departments/<str:page>/', views.departments, name='departments'),
    path('<str:departments>/', views.application, name='applications'),
    path('applications/<str:project>/', views.projectpage, name='projectpage')

]

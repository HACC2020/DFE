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

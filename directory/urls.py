from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('departments/<str:page>/', views.departments, name='departments'),
    path('<str:departments>/', views.application, name='applications'),
    path('applications/<str:project>/', views.projectpage, name='projectpage')

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about')
    #above is just a test
    #path('', views.directory, name='directory'),
    #path('about/', views.about, name='about')
]

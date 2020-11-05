from django.shortcuts import render

# Create your views here.
#def work(request, folder_id):

#does organization exist within database

def about(request):
    return render(request, 'about.html')
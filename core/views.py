from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'homePage.html')

def no_permission(request):
    return render(request, 'noPermission.html')

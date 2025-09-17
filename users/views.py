from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import Registration
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def Sign_Up(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration created successfully!")
            return redirect("log-in") 
    else:
        form = Registration()

    context = {
        "form" : form
    }   
    return render(request, 'registration/SignUp.html', context)
    
def Log_In(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            # Add an error message
            messages.error(request, "Invalid username or password")

    # Always return something (GET request or failed login)
    return render(request, 'registration/LogIn.html')

def Log_Out(request):
    if request.method == "POST":
        logout(request)
        return redirect('log-in')




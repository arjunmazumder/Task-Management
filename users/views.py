from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import Registration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from users.forms import LoginForm
from django.contrib.auth.tokens import default_token_generator


#Sign Up for user
def Sign_Up(request):

    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            # user.is_active = True
            user.save()
            messages.success(request, 'A Confirmation mail sent. Please check your email')
            return redirect("log-in") 
    else:
        form = Registration()

    context = {
        "form" : form
    }   
    return render(request, 'registration/SignUp.html', context)

#Log In for user
def Log_In(request):

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
        else:
            # Add an error message
            messages.error(request, "Invalid username or password")
    else:
        form = LoginForm() 
    context = {
        "form":form
    }    
    # Always return something (GET request or failed login)
    return render(request, 'registration/LogIn.html', context)

#Log Out for user
@login_required
def Log_Out(request):
    if request.method == "POST":
        logout(request)
        return redirect('log-in')
    return render(request, "registration/LogIn.html")
    

def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('log-in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')
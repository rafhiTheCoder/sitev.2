from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        
        if form.is_valid():
            form.save()
            
            # Get the username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            # Authenticate the user
            user = authenticate(response, username=username, password=password)
            
            # Log the user in
            if user is not None:
                login(response, user)
                return redirect("/")
            else:
                print("Authentication failed")
        else:
            print("Form is not valid")
    else:
        form = RegisterForm()
    
    return render(response, "register/register.html", {"form": form})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'index.html')

def login_view(request):
    print("view is hit")
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        print("User is authenticated")
        # Redirect to home if the user is logged in
        return redirect('/')  # Change 'home' to the name of your homepage view
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user
            login(request, form.get_user())
            return redirect('/')  # Or use 'next' if applicable
    else:
        form = AuthenticationForm()

    return render(request, 'templates/registration/login.html', {'form': form})
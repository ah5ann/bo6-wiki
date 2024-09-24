from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'index.html')

def login_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        print("User is authenticated")
        # Redirect to home if the user is logged in
        return redirect('/')  # Ensure 'Home' is the correct name for your homepage URL
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user
            login(request, form.get_user())
            # Get the next URL or default to home
            next_url = request.POST.get('next', '/')  # Default to 'Home'
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    # Pass the 'next' parameter to the template if available
    next_url = request.GET.get('next', '')
    
    return render(request, 'templates/registration/login.html', {'form': form, 'next': next_url})
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """register a new user"""
    if request.method != 'POST':
        # Display blank form
        form = UserCreationForm(); 
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST); 

        if form.is_valid():
            new_user = form.save(); 
            # Log the user in and redirect to the home page
            login(request, new_user); 
            return redirect('main_hub:index'); 

    context = {'form': form}; 
    return render(request, 'registration/register.html', context); 
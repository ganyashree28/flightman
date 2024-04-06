from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight
from .forms import FlightForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def dashboard(request):
    # Logic for the dashboard view
    return render(request, 'flights/dashboard.html')

@login_required 
def flight_list(request):
    # Fetch all flights from the database
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})

@login_required 
def flight_create(request):
    # Create a new flight instance
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flights/flight_form.html', {'form': form, 'operation': 'Create'})

@login_required 
def flight_update(request, pk):
    # Update an existing flight instance
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flights/flight_form.html', {'form': form, 'operation': 'Update'})

@login_required 
def flight_delete(request, pk):
    # Delete an existing flight instance
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'flights/flight_confirm_delete.html', {'flight': flight})

# flights/views.py

# Add this function to your views
def about(request):
    return render(request, 'flights/about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('flight_list')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'flights/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'flights/login.html')
        
def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password_confirm = request.POST['password2']

        if password == password_confirm:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('flight_list')
        else:
            return render(request, 'flights/signup.html', {'error': 'Passwords do not match.'})
    else:
        return render(request, 'flights/signup.html')
        
def logout_user(request):
    logout(request)
    return redirect('login') 
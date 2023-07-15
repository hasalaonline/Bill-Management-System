from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import WaitingList, ApprovedUser
from app.models import CEB,NWSDB

from bill_management_system import settings
# Create your views here.

def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']

        waitinguser = WaitingList(email=email, name=name)
        waitinguser.save()
        
        messages.success(request, "You have successfully added to the waiting list")
        return redirect('home')
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        fname = request.POST['fname']
        lname = request.POST['lname']

        approved_users = ApprovedUser.objects.values_list('email', flat=True)
        if email not in approved_users:
            messages.error(request, "You are currently not in our waitinglist")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')
        
        if len(username) > 20:
            messages.error(request, "Username must be under 10 characters")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        user = CEB(username=username, meter_readings={"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": "0", "7": 0, "8": "0", "9": 0, "10": 0, "11": 0, "12": 0}, units={"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": "0", "7": 0, "8": "0", "9": 0, "10": 0, "11": 0, "12": 0})
        user.save()

        user = NWSDB(username=username, meter_readings={"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": "0", "7": 0, "8": "0", "9": 0, "10": 0, "11": 0, "12": 0}, units={"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": "0", "7": 0, "8": "0", "9": 0, "10": 0, "11": 0, "12": 0})
        user.save()

        messages.success(request, "Your account has been successfully created. We have sent you an email for verification.")

        return redirect('signin')


    return render(request, 'authentication/signup.html')


def main(request):

    return render(request, 'main/main.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            fname = user.first_name
            return redirect('main')
        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect('signin')
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('home')

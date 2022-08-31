from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from notes import urls
from .forms import SignUpForm

# Create your views here.
def startup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user != None:
            login(request, user)
            return redirect(reverse('list'))
        else:
            messages.error(request, 'Credentials does not match.')
            return redirect(reverse('start'))
    return render(request, 'welcome.html', {})

def signup(request):
    if request.method == 'POST':
        # form = SignUpForm(request.POST or None)
        # if form.is_valid():
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']

            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()

            messages.success(request, 'Your account has been created successfully.')
            return redirect(reverse('start'))
    # else:
    #     form = SignUpForm()
    #     context = {'form':form}        
    return render(request, 'signup.html', {})

def signout(request):
    logout(request)
    request.user = None
    return redirect(reverse('start'))
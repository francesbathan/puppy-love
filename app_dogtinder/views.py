from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request): # renders homepage
    return render(request, 'home.html')

def login(request): # renders login page
    return render(request, 'login.html')

def process_login(request): #processes login page + validation
    form = request.POST
    print("hello")
    login_errors = User.objects.login_validator(form)
    if len(login_errors) > 0:
        request.session['login_error'] = False
        for login_error in login_errors.values():
            messages.error(request, login_error)
        return redirect('/login')
    user_id = User.objects.get(username=form['username']).id
    request.session['user_id'] = user_id
    return redirect('/dashboard')

def registration(request): # renders registration form
    return render(request, 'registration.html')

def process_registration(request): #process for registration form + validation
    form = request.POST
    errors_returned = User.objects.register_validator(form) 
    if len(errors_returned) > 0:
        request.session['register_error'] = True
        for single_error in errors_returned.values():
            messages.error(request, single_error)
        return redirect('/register')
    hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode() #hashes password so it doesn't display on the database
    new_user = User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'], username=form['username'],  password=hashed_pw)
    request.session['user_id'] = new_user.id
    return redirect('/add_dog')

def terms(request): # renders terms and conditions page
    return render(request, 'terms.html')

def add_dog(request): # renders form for user to add a dog
    return render(request, 'add_dog.html')

def process_dog(request):
    form = request.POST
    errors_returned = Dog.objects.dog_validator(form) 
    if len(errors_returned) > 0:
        request.session['dog_error'] = True
        for single_error in errors_returned.values():
            messages.error(request, single_error)
        return redirect('/add_dog')
    if request.method == 'POST':
        photo = request.FILES['image']
        new_dog = Dog.objects.create(dog_name=form['dog_name'], age=form['age'], breed=form['breed'], city=form['city'],  state=form['state'], zipcode=form['zipcode'], description=form['description'], dog=User.objects.get(id=request.session['user_id']), photo=photo)
    return redirect('/dashboard') 

def dashboard(request): # renders dashboard 
    return render(request, 'dashboard.html')

def dog_profile(request): # renders dog's profile page
    return render(request, 'profile.html')

def edit(request): # renders edit profile for dog
    return render(request, 'edit_dog.html')

def how(request): # renders how it works page
    return render(request, 'how.html')

def contact(request): # renders contact us page
    return render(request, 'contact.html')

def match(request): # renders matchpup page (no features available yet, just ad)
    return render(request, 'match.html')

def another_dog(request): # renders form inside logged in session to add a dog if user has not added one yet, or to add another dog
    return render(request, 'more_dog.html')

def account_settings(request): # renders page for user to be able to edit their account info
    return render(request, 'account_settings.html')

def logout(request): # logs user out of session and redirects to login page
    request.session.clear()
    return redirect('/login')
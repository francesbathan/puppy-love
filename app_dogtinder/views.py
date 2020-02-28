from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.db.models import Avg
import bcrypt
import statistics


def index(request): # renders homepage
    return render(request, 'home.html')

def login(request): # renders login page
    return render(request, 'login.html')

def process_login(request): #processes login page + validation
    form = request.POST
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
        return redirect('/registration')
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
        new_dog = Dog.objects.create(dog_name=form['dog_name'], age=form['age'], breed=form['breed'], city=form['city'],  state=form['state'], zipcode=form['zipcode'], description=form['description'], user=User.objects.get(id=request.session['user_id']), photo=photo)
    return redirect('/dashboard') 

def dashboard(request): # renders dashboard 
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'dogs': Dog.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id']),
        'total_ratings': len(RatingList.objects.all()),
        'next_dog': next_dog
    }
    return render(request, 'dashboard.html', context)

def next_dog(request, id):
    if 'user_id' not in request.session:
        return redirect('/login')
    total_dogs = len(Dog.objects.all())
    current_dog = Dog.objects.get(id=id)
    try:
        next_dog = Dog.get_next_by_created_at(current_dog)
    except:
        return redirect('/dashboard')
    context = {
        'dog': next_dog,
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'next_dog.html', context)

def process_rating(request, id): #processes/saves the ratings for the dogs
    form=request.POST
    rate_list = []
    rating = RatingList.objects.create(rating=form['rating'], dog=Dog.objects.get(id=id))
    rate_list.append(rating)
    return redirect('/dashboard')

def dog_profile(request, id): # renders dog's profile page
    if 'user_id' not in request.session:
        return redirect('/login')
    total_ratings = {}
    current_user = User.objects.get(id=request.session['user_id'])
    for dog in current_user.dogs.all():
        total = 1
        for rating in dog.ratings.all():
            total += rating.rating
        total_ratings[dog.id] = len(dog.ratings.all())/total
    context = {
        'current_user': current_user,
        'ratings_dict': total_ratings,
    }
    return render(request, 'profile.html', context)

def edit(request, id): # renders edit profile for dog
    if 'user_id' not in request.session:
        return redirect('/login')
    # errors_returned = Dog.objects.dog_validator(form) 
    # if len(errors_returned) > 0:
    #     request.session['dog_error'] = True
    #     for single_error in errors_returned.values():
    #         messages.error(request, single_error)
    #     return redirect(f'/edit/{dog.id}')
    context = {
        'dogs': Dog.objects.all(),
        'current_dog': Dog.objects.get(id=id),
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'edit_dog.html', context)

def dog_update(request, id): #processes the information that went through the form and redirects to the dog profile page
    form = request.POST
    print("test")
    current_dog=Dog.objects.get(id=id)
    current_dog.dog_name=form['dog_name']
    current_dog.age=form['age']
    current_dog.breed=form['breed']
    current_dog.city=form['city']
    current_dog.state=form['state']
    current_dog.zipcode=form['zipcode']
    current_dog.description=form['description']
    if request.FILES.get('image'):
        current_dog.photo=request.FILES['image']
    print("request", request.FILES)
    print(request.FILES)
    current_dog.save()
    return redirect(f'/dog_profile/{current_dog.id}')

def how(request): # renders how it works page
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'dogs': Dog.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'how.html', context)

def contact(request): # renders contact us page
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'dogs': Dog.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'contact.html', context)

def match(request): # renders matchpup page (no features available yet, just ad)
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'dogs': Dog.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'match.html', context)

def another_dog(request): # renders form inside logged in session to add a dog if user has not added one yet, or to add another dog
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'dogs': Dog.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'more_dog.html', context)

def process_dog_add(request):
    form = request.POST
    errors_returned = Dog.objects.dog_validator(form) 
    if len(errors_returned) > 0:
        request.session['dog_error'] = True
        for single_error in errors_returned.values():
            messages.error(request, single_error)
        return redirect('/add_dog')
    if request.method == 'POST':
        photo = request.FILES['image']
        current_user=User.objects.get(id=request.session['user_id'])
        new_dog = Dog.objects.create(dog_name=form['dog_name'], age=form['age'], breed=form['breed'], city=form['city'],  state=form['state'], zipcode=form['zipcode'], description=form['description'], user=User.objects.get(id=request.session['user_id']), photo=photo)
    return redirect(f'/dog_profile/{current_user.id}') 

def account_settings(request): # renders page for user to be able to edit their account info
    if 'user_id' not in request.session:
        return redirect('/login')
    context = {
        'dogs': Dog.objects.all(),
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'account_settings.html', context)

def process_account(request, id):
    form = request.POST
    user=User.objects.get(id=id)
    user.first_name=form['first_name']
    user.last_name=form['last_name']
    user.username=form['username']
    user.email=form['email']
    hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode() 
    user.password=hashed_pw
    user.save()
    return redirect(f'/dashboard')


def logout(request): # logs user out of session and redirects to login page
    request.session.clear()
    return redirect('/login')
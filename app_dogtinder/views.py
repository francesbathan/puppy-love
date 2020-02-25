from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def add_dog(request):
    return render(request, 'add_dog.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def dog_profile(request):
    return render(request, 'profile.html')

def how(request):
    return render(request, 'how.html')

def contact(request):
    return render(request, 'contact.html')

def match(request):
    return render(request, 'match.html')
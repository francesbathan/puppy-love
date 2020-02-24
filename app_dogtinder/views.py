from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def add_dog(request):
    return render(request, 'add_dog.html')
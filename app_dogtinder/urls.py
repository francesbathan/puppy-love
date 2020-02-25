from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #home intro
    path('login', views.login), #login form
    path('registration', views.registration), #registration form
    path('terms', views.terms), #terms & conditions page
    path('add_dog', views.add_dog), #add a dog form
    path('dashboard', views.dashboard), #homepage/dashboard
    path('dog_profile', views.dog_profile), #dog's profile
    path('how', views.how), #how it works page
    path('contact', views.contact), #contact us page
    path('match', views.match), #match up page
    path('add_another_dog', views.another_dog), #add another dog/add a dog if initial form was not filled out
    path('logout', views.logout), #logout button
]

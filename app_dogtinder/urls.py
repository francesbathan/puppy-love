from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #home intro
    path('login', views.login), #login form
    path('process_login', views.process_login), #processes login information
    path('registration', views.registration), #registration form
    path('process_registration', views.process_registration), #processes registration information
    path('terms', views.terms), #terms & conditions page
    path('add_dog', views.add_dog), #add a dog form
    path('process_dog', views.process_dog), #processes dog form
    # path('dog_upload', views.dog_upload), #file upload path
    path('dashboard', views.dashboard), #homepage/dashboard
    path('dog_profile', views.dog_profile), #dog's profile
    path('edit', views.edit), #edit dog profile form
    path('how', views.how), #how it works page
    path('contact', views.contact), #contact us page
    path('match', views.match), #match up page
    path('add_another_dog', views.another_dog), #add another dog/add a dog if initial form was not filled out
    path('account_settings', views.account_settings), #user's account settings
    path('logout', views.logout), #logout button
]
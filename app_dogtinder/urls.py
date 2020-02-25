from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #home intro
    path('login', views.login), #login form
    path('registration', views.registration), #registration form
    path('add_dog', views.add_dog), #add a dog form
    path('dashboard', views.dashboard), #homepage/dashboard
    path('dog_profile', views.dog_profile), #dog's profile
    path('how', views.how), #how it works page
    path('contact', views.contact), #contact us page
    path('match', views.match), #match up page

]

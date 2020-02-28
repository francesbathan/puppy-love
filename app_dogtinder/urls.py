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
    path('process_dog', views.process_dog), #processes dog form w/ file upload
    path('dashboard', views.dashboard), #homepage/dashboard
    path('next_dog/<int:id>', views.next_dog), #renders next dog
    path('process_rating/<int:id>', views.process_rating), #processes rating
    path('dog_profile/<int:id>', views.dog_profile), #current dog's profile
    path('edit/<int:id>', views.edit), #edit dog profile form
    path('dog_update/<int:id>', views.dog_update), #processes edit dog form
    path('how', views.how), #how it works page
    path('contact', views.contact), #contact us page
    path('match', views.match), #match up page
    path('add_another_dog', views.another_dog), #add another dog/add a dog if initial form was not filled out
    path('process_dog_add', views.process_dog_add), #processes dog from inside logged in session
    path('account_settings', views.account_settings), #user's account settings
    path('process_account/<int:id>', views.process_account), #processes edit account
    path('logout', views.logout), #logout button
]
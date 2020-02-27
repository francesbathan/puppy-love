from django.db import models
import re
import bcrypt


class UserManager(models.Manager): #validation for user login/registration
    def register_validator(self, post_data): #validator for registration form
        user_errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 2: #if first name is less than 2 characters
            user_errors['first_name'] = 'Please enter a valid first name.'
        if len(post_data['last_name']) < 2: #if last name is less than 2 characters
            user_errors['last_name'] = 'Please enter a valid last name.'
        if not EMAIL_REGEX.match(post_data['email']): # tests whether a field matches the pattern
            user_errors['email'] = "Please enter a valid email address."
        if len(post_data['username']) < 6: #if username  is less than 6 characters
            user_errors['username'] = 'Username must be more than 6 characters.'
        if len(post_data['password']) < 6: #if password is less than 6 characters
            user_errors['password'] = "Password must be more than 6 characters." #error message for password less than 6 characters
        if post_data['password'] != post_data['confirm_pw']: #checks if password and confirm password match
            user_errors['confirm_pw'] = "Passwords do not match. Try again."
        checked = False
        try:
            post_data['terms']
        except:
            user_errors['terms'] = "Please agree to the terms and conditions."
        return user_errors

    def login_validator(self, post_data): #validator for login form
        errors = {}
        current_user = User.objects.filter(username=post_data['username']) #defines variable for user
        if len(current_user) < 1: #checks if username is in the database and matches user input
            errors['username'] = 'Username does not exist.'
        elif not bcrypt.checkpw(post_data['password'].encode(), current_user[0].password.encode()): #takes in what user puts in the password field and checks if password matches with username in the database
            errors['password'] = "Username and password do not match."
        return errors

class DogManager(models.Manager): #validation for dog info entered
    def dog_validator(self, post_data):
        errors = {} 
        if len(post_data['dog_name']) < 1:
            errors['dog_name'] = "Please enter your dog's name."
        if len(post_data['age']) < 1:
            errors['age'] = "Please enter your dog's age."
        if len(post_data['age']) > 2:
            errors['age'] = "Please enter a valid age for your dog, as much as we'd love for all dogs to live forever."
        if len(post_data['breed']) < 1:
            errors['breed'] = "Please enter your dog's breed."
        if len(post_data['city']) < 1:
            errors['city'] = "Please enter a valid city."
        if len(post_data['state']) < 1:
            errors['state'] = "Please enter a valid state."
        if len(post_data['state']) > 2:
            errors['state'] = "Please enter a valid state."
        if len(post_data['description']) < 3:
            errors['description'] = "You gotta like your dog more than that." 
        return errors

class User(models.Model): #class for the user
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Dog(models.Model): #class for the dog
    dog_name = models.CharField(max_length=45)
    age = models.CharField(max_length=2)
    breed = models.CharField(max_length=255)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    description = models.TextField()
    photo = models.ImageField(upload_to="dogs")
    user = models.ForeignKey(User, related_name="dogs", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    objects = DogManager()

class RatingList(models.Model):
    rating = models.IntegerField()
    dog = models.ForeignKey(Dog, related_name="ratings", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

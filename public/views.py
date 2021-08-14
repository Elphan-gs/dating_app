from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Extension to connect in firebase
import pyrebase

# Pyrebase Handling Exceptions
import requests

config = {
    'apiKey': "AIzaSyAmv4gX8GqlKh8eoujKgu5gk0d67z3qpeg",
    'authDomain': "v1-dating.firebaseapp.com",
    'databaseURL': "https://v1-dating-default-rtdb.firebaseio.com",
    'projectId': "v1-dating",
    'storageBucket': "v1-dating.appspot.com",
    'messagingSenderId': "207145145137",
    'appId': "1:207145145137:web:9d7157953d82d105365610",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


class Signup(forms.Form):
    # Email
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': "Enter email address"
    }), required=True)

    # Password
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Enter Password"
    }), required=True)

    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Confirm Password"
    }))


class Login(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': "Enter email"
    }), required=True)

    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Enter password"
    }))


# Create your views here.
def index(request):
    # Write
    return render(request, 'public/index.html', {
        'head_nav': "Bump - Home Page"
    })


def about(request):
    return render(request, 'public/about.html', {
        'head_nav': "Bump - About Page"
    })


def contact(request):
    return render(request, 'public/contact.html', {
        'head_nav': "Bump - Contact Page"
    })


def download(request):
    return render(request, 'public/download.html', {
        'head_nav': "Bump - Download Page"
    })


def login(request):
    if request.method == "POST":
        login_form = Login(request.POST)

        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            auth.sign_in_with_email_and_password(email, password)

            request.session['user_info'] = auth.current_user

            return HttpResponseRedirect(reverse('user:index'))

        else:
            return render(request, 'public/login.html', {
                'head_nav': "Bump - Login Page",
                'form': login_form
            })

    return render(request, 'public/login.html', {
        'head_nav': "Bump - Login Page",
        'form': Login()
    })


def signup(request):
    if request.method == "POST":
        signup = Signup(request.POST)

        if signup.is_valid():
            email = signup.cleaned_data["email"]
            password = signup.cleaned_data["password"]
            confirm_password = signup.cleaned_data["confirm_password"]

            if password == confirm_password:
                auth.create_user_with_email_and_password(email=email, password=password)
            else:
                return render(request, 'public/signup.html', {
                    'head_nav': "Bump - Signup Page",
                    'form': signup,
                    'error_message': "Password and Confirm Password does not match."
                })

            return HttpResponseRedirect(reverse('public:signup'))
        else:
            return render(request, 'public/signup.html', {
                'head_nav': "Bump - Signup Page",
                'form': signup
            })

    return render(request, 'public/signup.html', {
        'head_nav': "Bump - Signup Page",
        'form': Signup()
    })

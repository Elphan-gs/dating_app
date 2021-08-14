from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.core.exceptions import *

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


# Create your views here.
def index(request):
    user_session = request.session['user_info']

    if user_session:
        pass
    else:
        pass

    print(f"Result: {request.session['user_info']}")

    return render(request, 'user/index.html', {
        'head_nav': "User - Home Page"
    })


def indepth_userinfo(request):
    return render(request, 'user/add_info.html', {
        'head_nav': "User - Additional Information"
    })


def logout(request):
    return HttpResponseRedirect(reverse('public:login'))

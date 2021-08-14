from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('download/', views.download, name="download"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
]

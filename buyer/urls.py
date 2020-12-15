from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    
    path('',csrf_exempt(Index.as_view()),name="index"),
    path('login',csrf_exempt(Login.as_view()),name="login"),
    path('register',csrf_exempt(Register.as_view()),name="register"),

   
    
]

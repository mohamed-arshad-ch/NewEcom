from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    
    path('',csrf_exempt(Index.as_view()),name="adminindex"),
    path('/getproductdetails',csrf_exempt(GetProductDetails.as_view()),name="getproductdetails"),
    path('/updateactive',csrf_exempt(UpdateActive.as_view()),name="updateactive"),
    

   
    
]

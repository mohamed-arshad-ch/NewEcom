from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    
    path('',csrf_exempt(VendorIndex.as_view()),name="vendorindex"),
    path('/getsubcategory',csrf_exempt(GetSubCategory.as_view()),name="getcategory"),
    path('/createcoupon',csrf_exempt(CreateCoupn.as_view()),name="getcategory"),
    path('/changestatus',csrf_exempt(ChageStatus.as_view()),name="changestatus")
   

   
    
]

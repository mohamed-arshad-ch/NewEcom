from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import auth
from .models import *
import json
from buyer.control import *

class Index(View):
    def get(self, request):
        try:
            categories = ChartOfAccounts.objects.filter(typeof=1)
            tax = ChartOfAccounts.objects.filter(typeof=3)
            products = Product.objects.all()
            return render(request,'mainadmin/admin_dashboard.html',{'category':categories,'tax':tax,'product':products})
        except Exception as e:
            print(e)
    @csrf_exempt
    def post(self, request):
        try:
            
            categoryvrate = Controlling.createcategory(self,categorydetail=request.POST)
            
            if categoryvrate == 1:
                 return JsonResponse({'type': 'success', 'message': 'Category Added Successfully'})
            else:
                 return JsonResponse({'type': 'success', 'message': 'Tax Added Successfully'})

        except Exception as e:
            print(e)
class GetProductDetails(View):
    def post(self, request):
        try:
            getallproductdetails = Controlling.getproductdetails(self,productid=request.POST)

            return JsonResponse({'detail':getallproductdetails})
        except Exception as e:
            print(e)

class UpdateActive(View):
    @csrf_exempt
    def post(self, request):
        try:
            print(request.POST)
            updateactivedetails = Controlling.updateactive(self,prod=request.POST)

            return JsonResponse({'type': 'success', 'message': 'All updated'})
        except Exception as e:
            print(e)
            return JsonResponse({'detail':"fsdf"})
from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import auth
from buyer.control import *

# Create your views here.
class VendorIndex(View):
    def get(self, request):
        try:
            if request.user.is_authenticated:
                chart = ChartOfAccounts.objects.all()
                return render(request,'vendor/vendor_dashboard.html',{'chart':chart})
            else:
                return redirect('index')
        except Exception as e:
            return HttpResponse(e)
    @csrf_exempt
    def post(self, request):
        try:
            productadding = Controlling.addproduct(self,productimage=request.FILES,productdetails=request.POST,user=request.user)
            if productadding == 1:
                return JsonResponse({'type':'warning','message':'Enter Your Valid Data'})
            else:
                return JsonResponse({'type':'success','message':'Product Added Successfully'})

            
        except Exception as e:
            print(e)
            return JsonResponse({'type':'success','message':e})
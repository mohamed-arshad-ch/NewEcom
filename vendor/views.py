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
                coupns = Coupon.objects.filter(user=request.user)
                products = Product.objects.filter(user=request.user)
                order = Order.objects.filter(current_status=True)
                orderitem = OrderItems.objects.all()
                
                        
                return render(request,'vendor/vendor_dashboard.html',{'chart':chart,'coupon':coupns,'products':products,'orders':order,'orderitem':orderitem})
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
            elif productadding == 2:
                return JsonResponse({'type':'success','message':'Product Added Successfully'})
            else:
                return JsonResponse({'type':'warning','message':'Exception Have'})


            
        except Exception as e:
            print(e)
            return JsonResponse({'type':'success','message':e})

class GetSubCategory(View):
    @csrf_exempt
    def post(self, request):
        try:
            getallsubcategory = Controlling.getsubcategoryall(self,category=request.POST)
            return JsonResponse({'dict':getallsubcategory})
        except Exception as e:
            print(e)

class CreateCoupn(View):
    @csrf_exempt
    def post(self, request):
        try:
            createcoups = Controlling.createcoupon(self,coupondetails=request.POST,user=request.user)
            if createcoups == 1:
                return JsonResponse({'type':'warning','message':'Enter Valid Data'})
            else:
                return JsonResponse({'type':'success','message':'Coupon Added Success','dict':createcoups})
        except Exception as e:
            print(e)
            return JsonResponse({'type':'warning','message':'Exception Have'})

class ChageStatus(View):
    def post(self, request):
        try:
            print(request.POST)
            productid = request.POST.get('product-id')
            status = request.POST.get('status')

            orderitem = OrderItems.objects.get(id=productid)
            orderitem.tracking_status = int(status)
            orderitem.save()
            return JsonResponse({'yes':'done'})
        except Exception as e:
            print(e)
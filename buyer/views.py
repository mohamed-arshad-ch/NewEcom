from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import auth
from .control import *
from .cart_controller import CretaeCart
import uuid
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
#index Page Loading

class Index(View):
    def get(self, request):
        try:
            try:
                newd = uuid.uuid1().int
                userid  = request.COOKIES['device']
                print(userid)
                
                if request.user.is_authenticated:
                    customer = Customer.objects.get(user=request.user)
                    order = Order.objects.get(current_status=False,customer=customer)
                    orderitem = OrderItems.objects.filter(order=order)
                    total = 0 
                    for order_item in orderitem:
                        actulprice = order_item.product.get_total()
                        withqty = order_item.qty * actulprice
                        total+= withqty
                    subcategory = SubCategory.objects.all()
                    category = ChartOfAccounts.objects.filter(typeof=1)
                    return render(request,'index.html',{'items':orderitem,'subtotal':total,'subcategory':subcategory,'category':category})
                else:
                    customer = Customer.objects.filter(custome_id=userid)
                    if customer.exists():
                        customerget = Customer.objects.get(custome_id=userid)
                        getorder = Order.objects.filter(customer=customerget,current_status=False)
                        if getorder.exists():
                            print("order exist")
                            orderis = Order.objects.get(customer=customerget,current_status=False)
                            
                        else:
                            print("not Exist")
                            order_create = Order.objects.create(customer=customerget,order_id=newd)
                            
                    else:
                        create_customer = Customer.objects.create(custome_id=userid)
                        order = Order.objects.filter(customer=create_customer,current_status=False)
                        if order.exists():
                            print("exist or")
                        else:
                            order_create = Order.objects.create(customer=create_customer,order_id=newd)
                        

                    total = 0 
                    customer_new = Customer.objects.get(custome_id=userid)
                    order_news = Order.objects.get(current_status=False,customer=customer_new)
                    orderitemk = OrderItems.objects.filter(order=order_news)
                    for order_item in orderitemk:
                        actulprice = order_item.product.get_total()
                        withqty = order_item.qty * actulprice
                        total+= withqty       
                        
                    subcategory = SubCategory.objects.all()
                    category = ChartOfAccounts.objects.filter(typeof=1)

                    return render(request,'index.html',{'items':orderitemk,'subtotal':total,'subcategory':subcategory,'category':category})

            except Exception as e:
                subcategory = SubCategory.objects.all()
                category = ChartOfAccounts.objects.filter(typeof=1)
                return render(request,'index.html',{'subcategory':subcategory,'category':category})
                
        except:
            subcategory = SubCategory.objects.all()
            category = ChartOfAccounts.objects.filter(typeof=1)
            return render(request,'index.html',{'subcategory':subcategory,'category':category})
   

#Login Page
class Login(View):
    def get(self, request):
        try:
            subcategory = SubCategory.objects.all()
            category = ChartOfAccounts.objects.filter(typeof=1)
            return render(request,'login.html',{'subcategory':subcategory,'category':category})
        except Exception as e:
            return HttpResponse(e)
    @csrf_exempt
    def post(self, request):
        userid  = request.COOKIES['device']
        try:
            try:
                user = CustomUser.objects.get(
                    email=request.POST.get('email'),password=request.POST.get('password'))
                print(user)
                if user is not None:
                    
                    
                    auth.login(request, user)
                    if user.user_type == True:
                        customer = Customer.objects.filter(user=user)
                        if customer.exists():
                            
                            return JsonResponse({'type': 'success', 'message': 'Login Successfully','customer_type':'customer'})
                        else:
                            customern, created = Customer.objects.get_or_create(custome_id=userid)
                            customern.user = user
                            customern.save()
                            return JsonResponse({'type': 'success', 'message': 'Login Successfully','customer_type':'customer'})

                        
                    else:
                        return JsonResponse({'type': 'success', 'message': 'Login Successfully','customer_type':'vendor'})

                else:
                    print(user)
                    return JsonResponse({'type': 'error', 'message': 'Invalid Username And Password'})

            except CustomUser.DoesNotExist:
                return JsonResponse({'type': 'error', 'message': 'Invalid Username And Password'})

        except Exception as e:
            print(e)
            return HttpResponse(e)
#Register Page
class Register(View):
    def get(self, request):
        try:
            subcategory = SubCategory.objects.all()
            category = ChartOfAccounts.objects.filter(typeof=1)
            return render(request,'register.html',{'subcategory':subcategory,'category':category})
        except Exception as e:
            return HttpResponse(e)
    
    @csrf_exempt
    def post(self,request):
        try:
            userid  = request.COOKIES['device']
            datas = request.POST
            checkandcreate = Controlling.createuser(self,registerdata=datas)
            
            
            if checkandcreate == 2:
                user = CustomUser.objects.get(email=datas.get('email'),password=datas.get('password'))
                if user is not None:
                    auth.login(request, user)
                    if user.user_type == True:
                        customer = Customer.objects.filter(user=user)
                        if customer.exists():
                            return JsonResponse({'type': 'success', 'message': 'Login Successfully','customer_type':'customer'})
                        else:
                            customern, created = Customer.objects.get_or_create(custome_id=userid)
                            customern.user = user
                            customern.save()
                            return JsonResponse({'type': 'success', 'message': 'Login Successfully','customer_type':'customer'})
                    else:
                        return JsonResponse({'type':'success','message':'Account Actived','customer_type':'vendor'})
                    
                else:
                    return JsonResponse({'type':'error','message':'User Not Login'})

            elif checkandcreate == 1:
                return JsonResponse({'type':'warning','message':'Enter Your Valid Data'})
            else:
                return JsonResponse({'type':'warning','message':'User Already Exist'})
                
            
            
        except Exception as e:
            return HttpResponse(e)

class ViewAllProducts(View):
    def get(self, request):
        try:
            subcategory = SubCategory.objects.all()
            category = ChartOfAccounts.objects.filter(typeof=1)
            products = Product.objects.filter(active=True)
            return render(request,'buyer/view_allproduct.html',{'product':products,'subcategory':subcategory,'category':category})
        except Exception as e:
            print(e)
            return HttpResponse(e)

class AddToCart(View):
    @csrf_exempt
    def post(self, request):
        try:
            
            addtocart = CretaeCart.createcartto(self,cartdetails=request.POST,user=request.user)
        except Exception as e:
            return e

class Logout(View):
    @csrf_exempt
    def post(self, request):
        try:
            
            auth.logout(request)
            return JsonResponse({'type':'success','message':'Logout Successfully'})

        except Exception as e:
            return e

class Cart(View):
    def get(self, request):
        try:
            subcategory = SubCategory.objects.all()
            category = ChartOfAccounts.objects.filter(typeof=1)
            userid  = request.COOKIES['device']
            if request.user.is_authenticated:
                customer = Customer.objects.get(user=request.user)
                order = Order.objects.get(current_status=False,customer=customer)
                orderitem = OrderItems.objects.filter(order=order)
                total = 0 
                for order_item in orderitem:
                    actulprice = order_item.product.get_total()
                    withqty = order_item.qty * actulprice
                    total+= withqty
                return render(request,'buyer/cart.html',{'items':orderitem,'subtotal':total,'subcategory':subcategory,'category':category})
            else:
                customer = Customer.objects.get(custome_id=userid)
                order = Order.objects.get(current_status=False,customer=customer)
                orderitem = OrderItems.objects.filter(order=order)
                total = 0 
                for order_item in orderitem:
                    actulprice = order_item.product.get_total()
                    withqty = order_item.qty * actulprice
                    total+= withqty
                
                return render(request,'buyer/cart.html',{'items':orderitem,'subtotal':total,'subcategory':subcategory,'category':category})
        except Exception as e:
            print(e)
            return render(request,'buyer/cart.html',{'subcategory':subcategory,'category':category})

class Checkout(View):
    def get(self, request):
        try:
            subcategory = SubCategory.objects.all()
            category = ChartOfAccounts.objects.filter(typeof=1)
            if request.user.is_authenticated:
                customer = Customer.objects.get(user=request.user)
                order = Order.objects.get(current_status=False,customer=customer)
                orderitem = OrderItems.objects.filter(order=order)
                total = 0 
                for order_item in orderitem:
                    actulprice = order_item.product.get_total()
                    withqty = order_item.qty * actulprice
                    total+= withqty
                return render(request,'buyer/checkout.html',{'items':orderitem,'subtotal':total,'subcategory':subcategory,'category':category})
            else:
                return redirect('login')
        except Exception as e:
            print(e)
    

class OrderSuccess(View):
    def get(self, request):
        try:
            return redirect('index')
        except Exception as e:
            print(e)
    def post(self, request):
        try:
            firstname = request.POST['first-name']
            lastname = request.POST['last-name']
            phone = request.POST['phone']
            email = request.POST['email']
            address = request.POST['address']
            town = request.POST['town']
            state = request.POST['state']
            postalcode = request.POST['postal-code']
            
            customer = Customer.objects.get(user=request.user)
            order = Order.objects.get(customer=customer,current_status=False)
            orderitems = OrderItems.objects.filter(order=order)
            billing = BillingAddress.objects.create(first_name=firstname,last_name=lastname,phone=phone,email=email,address=address,town=town,state=state,post_code=postalcode,order=order,customer=customer)

            order.current_status = True
            order.save()
            
            return render(request,'buyer/order-success.html',{'items':orderitems,'orderid':order})
        except Exception as e:
            print(e)

class AddWishlist(View):
    def get(self, request):
        try:
            if request.user.is_authenticated:
                wishlist = Wishlist.objects.filter(user=request.user)
                return render(request,'buyer/wishlist.html',{'product':wishlist})
            else:
                return redirect('login')
        except Exception as e:
            print(e)



class Invoice(View):
    def get(self, request):
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.filter(current_status=True,customer=customer).latest('dateandtime')
        print(order)
        orderitem = OrderItems.objects.filter(order=order)
        billingaddress = BillingAddress.objects.filter(order=order).latest('datetime')
        for i in orderitem:
            total = 0
            total+= i.total_qty_wise()
        data = {
            'customer':customer,
            'order':order,
            'orderitem':orderitem,
            'subtotal':total,
            'billing':billingaddress
        }
       
        return render(request,'buyer/invoice.html',data)

        
class GategoryWiseProduct(View):
    def get(self,request,id):
        try:
            subcategory = SubCategory.objects.all()
            newcategory = ChartOfAccounts.objects.filter(typeof=1)
            category = ChartOfAccounts.objects.get(id=id)
            products = Product.objects.filter(category=category)
            return render(request,'buyer/view_allproduct.html',{'product':products,'subcategory':subcategory,'category':newcategory})
        except Exception as e:
            print(e)
class SubGategoryWiseProduct(View):
    def get(self,request,id):
        try:
            newsubcategory = SubCategory.objects.all()
            category = ChartOfAccounts.objects.filter(typeof=1)
            subcategory = SubCategory.objects.get(id=id)
            products = Product.objects.filter(subcategory=subcategory)
            return render(request,'buyer/view_allproduct.html',{'product':products,'subcategory':newsubcategory,'category':category})
        except Exception as e:
            print(e)
        
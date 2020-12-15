from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import auth
from .control import *

#index Page Loading

class Index(View):
    def get(self, request):
        try:
            return render(request,'index.html')
        except Exception as e:
            return HttpResponse(e)
   

#Login Page
class Login(View):
    def get(self, request):
        try:
            return render(request,'login.html')
        except Exception as e:
            return HttpResponse(e)
    @csrf_exempt
    def post(self, request):
        try:
            try:
                user = CustomUser.objects.get(
                    email=request.POST.get('email'),password=request.POST.get('password'))
                print(user)
                if user is not None:
                    
                    
                    auth.login(request, user)
                    if user.user_type == True:
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
            
            return render(request,'register.html')
        except Exception as e:
            return HttpResponse(e)
    
    @csrf_exempt
    def post(self,request):
        try:
            datas = request.POST
            checkandcreate = Controlling.createuser(self,registerdata=datas)
            
            
            if checkandcreate == 2:
                user = CustomUser.objects.get(email=datas.get('email'),password=datas.get('password'))
                if user is not None:
                    auth.login(request, user)
                    if user.user_type == True:
                        return JsonResponse({'type':'success','message':'Account Actived','customer_type':'customer'})
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
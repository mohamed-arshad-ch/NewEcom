from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *
urlpatterns = [
    
    path('',csrf_exempt(Index.as_view()),name="index"),
    path('login',csrf_exempt(Login.as_view()),name="login"),
    path('register',csrf_exempt(Register.as_view()),name="register"),
    path('products',csrf_exempt(ViewAllProducts.as_view()),name="products"),
    path('addtocart',csrf_exempt(AddToCart.as_view()),name="addtocart"),
    path('logout',csrf_exempt(Logout.as_view()),name="logout"),
    path('cart',csrf_exempt(Cart.as_view()),name="cart"),
    path('checkout',csrf_exempt(Checkout.as_view()),name="checkout"),
    path('ordersuccess',csrf_exempt(OrderSuccess.as_view()),name="ordersuccess"),
    path('wishlist',csrf_exempt(AddWishlist.as_view()),name="wishlist"),
    path('invoice',csrf_exempt(Invoice.as_view()),name="invoice"),
    path('category/<int:id>',csrf_exempt(GategoryWiseProduct.as_view()),name="category"),
    path('subcategory/<int:id>',csrf_exempt(SubGategoryWiseProduct.as_view()),name="subcategory"),






    

   
    
]

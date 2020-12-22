from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_type = models.BooleanField(blank=False,null=False,default=True)

    def __str__(self):
        return self.username

class ChartOfAccounts(models.Model):
    name = models.CharField(max_length=100)
    typeof = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(ChartOfAccounts,on_delete=models.CASCADE,related_name="categorytype")
    active = models.BooleanField(default=True)



class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    category = models.ForeignKey(ChartOfAccounts,on_delete=models.CASCADE,related_name='category')
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='subcategory')
    tag = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    discount = models.IntegerField()
    tax = models.ForeignKey(ChartOfAccounts,on_delete=models.CASCADE,related_name='tax')
    attr_name = models.CharField(max_length=100)
    attr_price = models.FloatField()
    attr_type = models.IntegerField()
    total_stock = models.IntegerField()
    available_stock = models.IntegerField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

   

    

    def get_total(self):

        total = 0
        
        ip = (self.price * self.discount)/100
        total = self.price - ip
        

        taxt_total = (total * int(self.tax.name))/100
        with_tax = total+taxt_total
        return with_tax
    

class Coupon(models.Model):
    date_cteadet = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    co_code = models.CharField(max_length=25)
    co_count = models.IntegerField()
    co_discount = models.IntegerField()
    co_used = models.IntegerField()
    co_exp = models.DateField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Customer(models.Model):
    date_created = models.DateField(auto_now_add=True)
    custome_id = models.CharField(max_length=150)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.custome_id

class Order(models.Model):
    date_created = models.DateField(auto_now_add=True)
    dateandtime = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=150)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    current_status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id

class OrderItems(models.Model):
    date_created = models.DateField(auto_now_add=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="all_pro")
    qty = models.IntegerField(default=0)
    active_status = models.BooleanField(default=False)
    tracking_status = models.IntegerField(default=1)

    

    def __str__(self):
        return self.product.name
    
    def total_qty_wise(self):
        total = 0
        price = self.product.get_total()
        
        total = self.qty * price
        
        return total

    # def main_total(self):

        
   
class BillingAddress(models.Model):
    date_created = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    town = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    post_code = models.CharField(max_length=150)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

class Wishlist(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="all_product")
    active_status = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

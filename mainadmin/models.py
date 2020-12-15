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

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    category = models.ForeignKey(ChartOfAccounts,on_delete=models.CASCADE,related_name='category')
    subcategory = models.ForeignKey(ChartOfAccounts,on_delete=models.CASCADE,related_name='subcategory')
    tag = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    discount = models.IntegerField()
    tax = models.ForeignKey(ChartOfAccounts,on_delete=models.CASCADE,related_name='tax')
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class ProductAttributes(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


    
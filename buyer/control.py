from mainadmin.models import *

class Controlling():

    def createuser(self,**kwargs):
        fname = kwargs['registerdata'].get('fname')
        lname = kwargs['registerdata'].get('lname')
        email = kwargs['registerdata'].get('email')
        password = kwargs['registerdata'].get('password')
        typeofuser = kwargs['registerdata'].get('typeofuse')

        
        useravailable = CustomUser.objects.filter(email=email).count()
        if useravailable == 0:
            if fname == '' and lname == '':
                return 1
            else:
                if int(typeofuser) == 1:
                    CustomUser.objects.create(username=email,email=email,password=password,first_name=fname,last_name=lname,user_type=True)
                    return 2
                else:
                    CustomUser.objects.create(username=email,email=email,password=password,first_name=fname,last_name=lname,user_type=False)
                    return 2

                
        else:
            return 3

        

    def addproduct(self,**kwargs):
        try:
            image = kwargs['productimage'].get('image')
            category = kwargs['productdetails'].get('category')
            subcategory = kwargs['productdetails'].get('subcategory')
            tag = kwargs['productdetails'].get('tag')
            description = kwargs['productdetails'].get('description')
            productname = kwargs['productdetails'].get('productname')
            price = kwargs['productdetails'].get('price')
            discount = kwargs['productdetails'].get('discount')
            tax = kwargs['productdetails'].get('tax')
            attrname = kwargs['productdetails'].get('attr_name')
            attrprice = kwargs['productdetails'].get('attr_price')
            attrtype = kwargs['productdetails'].get('attr_type')
            stock = kwargs['productdetails'].get('stock')
            print(stock)
            print(attrtype)
            user = kwargs['user']
            
            print(category,subcategory,tax)
            maincategory = ChartOfAccounts.objects.get(name=category)
            mainsubcategory = SubCategory.objects.get(name=subcategory)
            maintax = ChartOfAccounts.objects.get(name=tax)

            if tag == "" and description == "" and productname == "" and price == "":
                return 1
            else:
                productdb = Product.objects.create(attr_name=attrname,attr_price=attrprice,attr_type=attrtype, image=image,name=productname,category=maincategory,subcategory=mainsubcategory,tag=tag,description=description,price=float(price),discount=discount,tax=maintax,user=user,total_stock=int(stock),available_stock=int(stock))
                return 2
        except Exception as e:
            print(e)
            return 3


    
#Create category in admin

    def createcategory(self, **kwargs):
        category = kwargs['categorydetail'].get('category')
        subcategory = kwargs['categorydetail'].get('subcategory')
        tax = kwargs['categorydetail'].get('tax')

        
        if tax == "":
            newcategory = ChartOfAccounts.objects.get_or_create(name=category,typeof=1,active=True)
            fetchcategory = ChartOfAccounts.objects.get(name=category)
            newsubcategory = SubCategory.objects.get_or_create(name=subcategory,active=True,category=fetchcategory)

            return 1
        else:
            newcategory = ChartOfAccounts.objects.get_or_create(name=category,typeof=1,active=True)
            fetchcategory = ChartOfAccounts.objects.get(name=category)
            newsubcategory = SubCategory.objects.get_or_create(name=subcategory,active=True,category=fetchcategory)
            newtax = ChartOfAccounts.objects.get_or_create(name=tax,typeof=3,active=True)

            return 2

    def getsubcategoryall(self,**kwargs):
        categoryname = kwargs['category'].get('category')
        

        category = ChartOfAccounts.objects.get(name=categoryname)
        subcategories = SubCategory.objects.filter(category=category)

        subcategorieslist = {'sub':[]}
        for i in subcategories:
            print(i.name)
            subcategorieslist['sub'].append(i.name)
        
        print(subcategorieslist)
        return subcategorieslist
        

#Get Product Details

    def getproductdetails(self,**kwargs):
        productid = kwargs['productid'].get('productid')
        products = Product.objects.get(id=int(productid))

        productdetails = {
            'subcategory':products.subcategory.name,
            'tag':products.tag,
            'desc':products.description,
            'discount':products.discount,
            'attr_name':products.attr_name,
            'attr_price':products.attr_price,
            'user':products.user.first_name,
            'active':products.active
        }
        return productdetails

#update Active details

    def updateactive(self,**kwargs):
        try:
            print(kwargs)
            productid = kwargs['prod'].getlist('newid')
            
        
            print(productid[0])
            productidsp = productid[0].replace(',', '')
            print(productidsp)

            for i in productidsp:
                newid = int(i)
                products = Product.objects.get(id=newid)
                products.active = True
                products.save()
            return 1
        except Exception as e:
            print(e)
    
    def createcoupon(self , **kwargs):
        try:
            name = kwargs['coupondetails'].get('name')
            secret = kwargs['coupondetails'].get('secret')
            discount = kwargs['coupondetails'].get('discount')
            count = kwargs['coupondetails'].get('count')
            date = kwargs['coupondetails'].get('date')
            user = kwargs['user']
            
            if len(name) == 0 and len(secret) == 0  and len(date) == 0:
                print("vhv")
                return 1
            else:
                coupon = Coupon.objects.create(name=name,user=user,co_code=secret,co_count=int(count),co_discount=int(discount),co_used=0,co_exp=date)

                coupondetails = {
                    'name':coupon.name,
                    'secret':coupon.co_code,
                    'used':coupon.co_used,
                    'count':coupon.co_count,
                    'discount':coupon.co_discount,
                    'date':coupon.co_exp,
                    
                }
                return coupondetails
        except Exception as e:
            print(e)


        
        


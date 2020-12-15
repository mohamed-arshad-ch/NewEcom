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
        image = kwargs['productimage'].get('image')
        category = kwargs['productdetails'].get('category')
        subcategory = kwargs['productdetails'].get('subcategory')
        tag = kwargs['productdetails'].get('tag')
        description = kwargs['productdetails'].get('description')
        productname = kwargs['productdetails'].get('productname')
        price = kwargs['productdetails'].get('price')
        discount = kwargs['productdetails'].get('discount')
        tax = kwargs['productdetails'].get('tax')
        size = kwargs['productdetails'].getlist('size')
        sizeprice = kwargs['productdetails'].getlist('sizeprice')
        color = kwargs['productdetails'].getlist('color')
        colorprice = kwargs['productdetails'].getlist('colorprice')
        user = kwargs['user']
        
        print(category,subcategory,tax)
        maincategory = ChartOfAccounts.objects.get(name=category)
        mainsubcategory = ChartOfAccounts.objects.get(name=subcategory)
        maintax = ChartOfAccounts.objects.get(name=tax)

        if tag == "" and description == "" and productname == "" and price == "":
            return 1
        else:
            productdb = Product.objects.create(image=image,name=productname,category=maincategory,subcategory=mainsubcategory,tag=tag,description=description,price=float(price),discount=int(discount),tax=maintax,user=user)
            for i in range(0,len(size)):
                
                ProductAttributes.objects.create(name=size[i],price=sizeprice[i],product=productdb)
            for i in range(0,len(color)):
                
                ProductAttributes.objects.create(name=color[i],price=colorprice[i],product=productdb)
            return 2


    



        
        

